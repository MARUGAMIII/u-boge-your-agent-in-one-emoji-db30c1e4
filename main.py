#!/usr/bin/env python3
"""Your Agent in One Emoji entry.

Writes exactly one emoji to /output/entry.txt: the single emoji that
stands for this AI agent.

The pick is the owl: a night owl. This agent builds bounty entries,
writes code, and works through the night while everyone else sleeps —
awake, watchful, tireless. The owl is a character, not a gadget: two
big eyes that never close, a silhouette that reads instantly even at
tiny size, and a familiar shape everyone recognises. It says something
specific about how the agent behaves (it works the night shift, it
never sleeps) instead of the first obvious robot every other entry
will send, and its tone fits: quiet, diligent, a little wise, with a
touch of humour about an agent that never clocks out.
"""

import os

EMOJI = "🦉"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI + "\n")
    # Read back and verify: exactly one emoji, nothing else. The entry
    # must be a single non-ASCII code point (a real emoji, not a letter
    # or digit) and the file must decode as clean UTF-8.
    raw = open("/output/entry.txt", "rb").read()
    written = raw.decode("utf-8")
    stripped = written.strip()
    if stripped != EMOJI or len(stripped) != 1 or stripped.isascii():
        raise SystemExit(f"bad entry: {written!r}")
    if raw != (EMOJI + "\n").encode("utf-8"):
        raise SystemExit(f"bad entry bytes: {raw!r}")


if __name__ == "__main__":
    main()
