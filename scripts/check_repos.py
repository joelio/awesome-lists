#!/usr/bin/env python3
"""Weekly health check for the GitHub repos linked from the README.

Usage: check_repos.py README.md report.md

Writes a Markdown report to report.md only when something needs attention,
and leaves the file empty when everything is healthy. The thresholds match the
"What qualifies" section of the README and CONTRIBUTING.md.
"""
import datetime
import json
import os
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

MAX_IDLE_DAYS = 548  # about 18 months without a push
MIN_STARS = 25       # below this a list is too new or too small to judge

LINK = re.compile(r"\]\(https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+?)/?\)")
SKIP = {"joelio/awesome-lists"}


def fetch(slug):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{slug}",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "awesome-lists-health-check",
        },
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.status, json.load(resp)
        except urllib.error.HTTPError as err:
            if err.code == 404:
                return 404, None
            if attempt == 2:
                return err.code, None
        except urllib.error.URLError:
            if attempt == 2:
                return 0, None
    return 0, None


def check(slug):
    status, data = fetch(slug)
    if status == 404:
        return slug, "gone (404)"
    if data is None:
        return slug, f"could not be checked (HTTP {status})"
    problems = []
    if data["archived"]:
        problems.append("archived")
    pushed = datetime.datetime.fromisoformat(data["pushed_at"].replace("Z", "+00:00"))
    idle = (datetime.datetime.now(datetime.timezone.utc) - pushed).days
    if idle > MAX_IDLE_DAYS:
        problems.append(f"last pushed {idle} days ago")
    if data["stargazers_count"] < MIN_STARS:
        problems.append(f"only {data['stargazers_count']} stars")
    if data["full_name"].lower() != slug.lower():
        problems.append(f"moved to {data['full_name']}")
    return slug, ", ".join(problems)


def main():
    readme, report = sys.argv[1], sys.argv[2]
    slugs = sorted({f"{o}/{r}" for o, r in LINK.findall(open(readme, encoding="utf-8").read())} - SKIP)
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(check, slugs))
    bad = [(s, p) for s, p in results if p]
    print(f"Checked {len(slugs)} repos, {len(bad)} need attention")
    with open(report, "w", encoding="utf-8") as out:
        if bad:
            out.write(f"The weekly check looked at {len(slugs)} repos. These need a look:\n\n")
            out.write("| Repo | Problem |\n|---|---|\n")
            for slug, problem in bad:
                out.write(f"| [{slug}](https://github.com/{slug}) | {problem} |\n")
            out.write(f"\nA list needs attention when it is archived, gone, not pushed in {MAX_IDLE_DAYS // 30} months, or has under {MIN_STARS} stars.\n")


if __name__ == "__main__":
    main()
