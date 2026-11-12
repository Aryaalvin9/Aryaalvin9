#!/usr/bin/env python3
"""Update README with recently pushed public repositories, using GitHub REST API."""
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

USERNAME = os.environ.get("GITHUB_USERNAME", "Aryaalvin9")
README = Path("README.md")
START = "<!-- ACTIVITY:START -->"
END = "<!-- ACTIVITY:END -->"


def fetch_repos():
    url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&sort=pushed&direction=desc&type=owner"
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "github-profile-updater"}
    token = os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urlopen(Request(url, headers=headers), timeout=30) as response:
        return json.load(response)


def main():
    content = README.read_text(encoding="utf-8")
    if START not in content or END not in content:
        raise SystemExit("README is missing ACTIVITY markers")
    repos = [r for r in fetch_repos() if not r.get("fork") and not r.get("archived") and r.get("name", "").lower() != USERNAME.lower()]
    repos = repos[:5]
    if repos:
        lines = []
        for repo in repos:
            name = repo["name"].replace("|", "\\|")
            description = (repo.get("description") or "Public repository").replace("\n", " ").replace("|", "\\|")
            description = description[:110]
            lang = repo.get("language") or "—"
            date = (repo.get("pushed_at") or "")[:10]
            lines.append(f"- **[{name}]({repo['html_url']})** — {description} · `{lang}` · Last push: {date}")
        section = "\n".join(lines)
    else:
        section = "_No public repositories with recent pushes to display yet._"
    before, tail = content.split(START, 1)
    _, after = tail.split(END, 1)
    updated = before + START + "\n" + section + "\n" + END + after
    if updated != content:
        README.write_text(updated, encoding="utf-8")
        print("README activity updated")
    else:
        print("README activity unchanged")


if __name__ == "__main__":
    main()
