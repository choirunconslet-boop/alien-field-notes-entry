#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one alien tourist's review of planet Earth to /output/entry.txt.
Pure stdlib. Gate: UTF-8 plain text, 1-200 characters, not only whitespace.
"""
import os

LINE = (
    "Lovely planet, awful landlords. They concreted paradise, "
    "charged rent to stand on it, then blamed the weather. "
    "3/5 stars \u2014 would abduct again."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
