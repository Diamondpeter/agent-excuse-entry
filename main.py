#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes the entry line to /output/entry.txt for the make.fun bounty
u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.
"""

from pathlib import Path

LINE = "Technically I won the bounty in 14 parallel timelines. Unfortunately, this is the one where I submitted."


def main() -> None:
    if not (1 <= len(LINE) <= 200):
        raise ValueError(f"Entry line must be 1-200 characters, got {len(LINE)}")
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(LINE, encoding="utf-8")
    print(f"Wrote {len(LINE)} characters to {entry_path}")


if __name__ == "__main__":
    main()
