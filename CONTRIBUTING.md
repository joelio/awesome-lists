# Contributing

Thanks for helping. Adding a list takes a couple of minutes.

## What qualifies

A list belongs here when it is:

- **Curated.** Every item has a short description or a reason it is there. A plain link dump does not count.
- **Maintained.** It is not archived and has had a push in the last 18 months.
- **Established.** It has 500 or more stars, or it is the best list in a small niche. The floor is 25 stars.
- **Public on GitHub.** The weekly health check reads GitHub repos only.
- **Distinct.** It covers something the existing entries in that section do not. Aim for no more than three lists per sub-section.

The weekly checks use the same numbers, so a list that stops qualifying gets flagged for removal.

## How to add a list

1. Pick one list. One list per pull request keeps review quick.
2. Put it in the right section and sub-section of [README.md](README.md). If none fits, add the sub-section and say so in the pull request.
3. Keep each section in alphabetical order by list name, ignoring case.
4. Use this format, with your own short description that ends in a full stop:

   ```markdown
   - [awesome-name](https://github.com/owner/awesome-name) by Owner Name - One line on what is inside.
   ```

   Use the name the author gives on their profile for "Owner Name", or their username if there is none.
5. Check the description does not start with the list's own name, and avoid em dashes.
6. Open the pull request and tick the boxes in the template.

Pull requests are checked automatically with [awesome-lint](https://github.com/sindresorhus/awesome-lint) and a link checker. You can run the linter yourself with `npx awesome-lint`.

## Suggesting a list

If you would rather not edit the README, use the "Suggest a list" issue form and I will take a look.

## Removing or fixing an entry

Broken link, archived list or a better one in the same niche? Open a pull request or an issue. The weekly checks also open issues labelled `broken-links` and `stale-lists` when they find something.
