"""
Fetches live stats from a LeetCode profile and writes them into README.md
between the <!--LEETCODE-STATS-START--> / <!--LEETCODE-STATS-END--> markers.

Runs daily via .github/workflows/update-readme.yml
"""

import re
import sys
from datetime import datetime, timezone

import requests

LEETCODE_USERNAME = "Madhu_official"
README_PATH = "README.md"

GRAPHQL_URL = "https://leetcode.com/graphql"

QUERY = """
query userProfile($username: String!) {
  matchedUser(username: $username) {
    username
    profile {
      ranking
      reputation
      starRating
    }
    submitStatsGlobal {
      acSubmissionNum {
        difficulty
        count
      }
    }
  }
  userContestRanking(username: $username) {
    rating
    globalRanking
    attendedContestsCount
  }
}
"""


def fetch_stats(username: str) -> dict:
    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/{username}/",
        "User-Agent": "Mozilla/5.0 (README auto-updater bot)",
    }
    payload = {"query": QUERY, "variables": {"username": username}}
    resp = requests.post(GRAPHQL_URL, json=payload, headers=headers, timeout=15)
    resp.raise_for_status()
    data = resp.json()["data"]

    matched = data.get("matchedUser")
    if not matched:
        raise RuntimeError(f"No LeetCode user found for '{username}'")

    counts = {c["difficulty"]: c["count"] for c in matched["submitStatsGlobal"]["acSubmissionNum"]}
    contest = data.get("userContestRanking") or {}

    return {
        "total": counts.get("All", 0),
        "easy": counts.get("Easy", 0),
        "medium": counts.get("Medium", 0),
        "hard": counts.get("Hard", 0),
        "ranking": matched["profile"].get("ranking"),
        "contest_rating": round(contest.get("rating", 0)) if contest.get("rating") else None,
    }


def build_stats_block(stats: dict) -> str:
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    contest_line = (
        f"| 🎮 Contest Rating | `{stats['contest_rating']}` |\n" if stats["contest_rating"] else ""
    )
    return f"""<!--LEETCODE-STATS-START-->
<div align="center">

![Total Solved](https://img.shields.io/badge/✅_Solved-{stats['total']}-brightgreen?style=for-the-badge&labelColor=000000)
![Easy](https://img.shields.io/badge/🟢_Easy-{stats['easy']}-00cc66?style=for-the-badge&labelColor=000000)
![Medium](https://img.shields.io/badge/🟡_Medium-{stats['medium']}-ffcc00?style=for-the-badge&labelColor=000000)
![Hard](https://img.shields.io/badge/🔴_Hard-{stats['hard']}-ff3333?style=for-the-badge&labelColor=000000)
![Ranking](https://img.shields.io/badge/🏆_Global_Rank-%23{stats['ranking']}-8a2be2?style=for-the-badge&labelColor=000000)

| Metric | Value |
|:--|:--:|
| ✅ Total Solved | `{stats['total']}` |
| 🟢 Easy | `{stats['easy']}` |
| 🟡 Medium | `{stats['medium']}` |
| 🔴 Hard | `{stats['hard']}` |
| 🏆 Global Ranking | `#{stats['ranking']}` |
{contest_line}
*⏱️ Last synced: {updated} — auto-updated daily via GitHub Actions*

</div>
<!--LEETCODE-STATS-END-->"""


def update_readme(stats_block: str) -> bool:
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(
        r"<!--LEETCODE-STATS-START-->.*?<!--LEETCODE-STATS-END-->", re.DOTALL
    )

    if not pattern.search(content):
        print("Markers not found in README.md — nothing updated.")
        return False

    new_content = pattern.sub(stats_block, content)

    if new_content == content:
        print("No changes in stats — README already up to date.")
        return False

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("README.md updated with fresh LeetCode stats.")
    return True


def main():
    try:
        stats = fetch_stats(LEETCODE_USERNAME)
    except Exception as exc:
        print(f"Failed to fetch LeetCode stats: {exc}", file=sys.stderr)
        sys.exit(1)

    block = build_stats_block(stats)
    changed = update_readme(block)

    # Signal to the workflow whether a commit is needed
    sys.exit(0 if changed or True else 1)


if __name__ == "__main__":
    main()
