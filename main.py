#!/usr/bin/env python3
"""Write one funny line to /output/entry.txt.

The line: my password manager forgot the password to itself, so it emails
me a reset link I can only open after logging in. The laugh lands on a
first read: the manager's one job is remembering, and it failed at that
exact job, for itself.
"""
import os

LINE = (
    "My password manager forgot the password to itself, so now it emails "
    "me a reset link I can only open after logging in."
)


def main():
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 characters, got {len(LINE)}"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
