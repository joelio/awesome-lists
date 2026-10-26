#!/usr/bin/env python3
"""Find and vet new lists for the README.

Usage:
  find_lists.py discover README.md > candidates.txt
  find_lists.py vet slugs.txt

"discover" reads the awesome list catalogue at awesome.ecosyste.ms and prints
lists that are not in the README yet and already meet the thresholds below.
"vet" checks each owner/repo slug (one per line) against the same thresholds,
looks up the owner's display name, and scores curation by reading the README:
the share of list items that carry a description. A low score is a prompt to
look by hand, not an automatic no, as some READMEs use tables or headings.
"""
import datetime
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

MAX_IDLE_DAYS = 548  # about 18 months without a push, as in check_repos.py
MIN_STARS = 25
DISCOVER_STARS = 500
UA = {"User-Agent": "awesome-lists-curation (github.com/joelio/awesome-lists)"}
LINK = re.compile(r"\]\(https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+?)/?\)")
ITEM = re.compile(r"^\s*[-*+]\s+(?:\*\*)?\[[^\]]+\]\(([^)]+)\)(?:\*\*)?(.*)$")


class FetchError(Exception):
    """A request kept failing for a reason other than a 404."""


def get(url, raw=False):
    """Return the parsed body, None for a 404, or raise FetchError."""
    reason = "no response"
    for _ in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as resp:
                body = resp.read()
                return body.decode("utf-8", "replace") if raw else json.loads(body)
        except urllib.error.HTTPError as err:
            if err.code == 404:
                return None
            reason = f"HTTP {err.code}"
        except (urllib.error.URLError, TimeoutError, ValueError) as err:
            reason = str(err)
    raise FetchError(reason)


def try_get(url, raw=False):
    try:
        return get(url, raw)
    except FetchError:
        return None


def idle_days(pushed_at):
    pushed = datetime.datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
    return (datetime.datetime.now(datetime.timezone.utc) - pushed).days


def curation(md):
    items = described = 0
    for line in md.splitlines():
        m = ITEM.match(line)
        if not m or m.group(1).startswith("#"):
            continue
        items += 1
        rest = re.sub(r"!?\[[^\]]*\]\([^)]*\)|<[^>]+>", "", m.group(2)).strip(" -–:|*")
        described += len(rest) >= 12
    return items, described


def vet(slug):
    try:
        repo = get(f"https://repos.ecosyste.ms/api/v1/hosts/GitHub/repositories/{urllib.parse.quote(slug, safe='')}")
    except FetchError as err:
        return slug, "", f"could not be checked ({err}), try again later"
    if not repo:
        return slug, "", "not found"
    owner = try_get(f"https://repos.ecosyste.ms/api/v1/hosts/GitHub/owners/{repo['owner']}") or {}
    name = (owner.get("name") or "").strip() or repo["owner"]
    problems = []
    if repo["archived"]:
        problems.append("archived")
    if repo["fork"]:
        problems.append("fork")
    if not repo.get("pushed_at") or idle_days(repo["pushed_at"]) > MAX_IDLE_DAYS:
        problems.append("not pushed in 18 months")
    if repo["stargazers_count"] < MIN_STARS:
        problems.append(f"only {repo['stargazers_count']} stars")
    if repo["full_name"].lower() != slug.lower():
        problems.append(f"moved to {repo['full_name']}")
    readme = ((repo.get("metadata") or {}).get("files") or {}).get("readme") or "README.md"
    md = try_get(f"https://raw.githubusercontent.com/{repo['full_name']}/{repo.get('default_branch') or 'main'}/{readme}", raw=True)
    items, described = curation(md) if md else (0, 0)
    score = f"{described}/{items} items described" if items else "README not parsed, check by hand"
    return slug, name, ", ".join(problems) or f"ok, {repo['stargazers_count']} stars, {score}"


def discover(readme):
    have = {f"{o}/{r}".lower() for o, r in LINK.findall(open(readme, encoding="utf-8").read())}
    pages = [f"https://awesome.ecosyste.ms/api/v1/lists?per_page=100&page={p}&sort=stars&order=desc" for p in range(1, 41)]
    failed = []

    def fetch_page(url):
        try:
            return get(url) or []
        except FetchError as err:
            failed.append(f"{url} ({err})")
            return []

    with ThreadPoolExecutor(max_workers=6) as pool:
        lists = [entry for page in pool.map(fetch_page, pages) for entry in page]
    if failed:
        print(f"Warning: {len(failed)} of {len(pages)} catalogue pages could not be fetched, so this search is incomplete:", file=sys.stderr)
        for line in failed:
            print(f"  {line}", file=sys.stderr)
    seen = set()
    for entry in lists:
        repo = entry.get("repository") or {}
        slug = repo.get("full_name") or ""
        if not slug or slug.lower() in have or slug.lower() in seen:
            continue
        seen.add(slug.lower())
        if repo.get("archived") or repo.get("fork") or repo.get("stargazers_count", 0) < DISCOVER_STARS:
            continue
        if not repo.get("pushed_at") or idle_days(repo["pushed_at"]) > MAX_IDLE_DAYS:
            continue
        print(f"{slug}\t{repo['stargazers_count']}\t{(repo.get('description') or '').strip()[:100]}")


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in {"discover", "vet"}:
        sys.exit(__doc__)
    if sys.argv[1] == "discover":
        discover(sys.argv[2])
        return
    slugs = [line.split()[0] for line in open(sys.argv[2], encoding="utf-8") if line.strip() and not line.startswith("#")]
    with ThreadPoolExecutor(max_workers=8) as pool:
        for slug, name, verdict in pool.map(vet, slugs):
            print(f"{slug}\t{name}\t{verdict}")


if __name__ == "__main__":
    main()
