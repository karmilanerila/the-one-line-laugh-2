"""The One-Line Laugh entry (second parallel angle).

Writes a single funny line to /output/entry.txt.
Stdlib only, fully deterministic: the same bytes every run.
The joke: technology that works all day and betrays you at the
exact worst moment — a universal everyday truth with a surprise twist.
"""

import os

LINE = "My Wi-Fi works perfectly all day, then disconnects the exact second my boss asks me a question."


def write_entry() -> str:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert text.strip(), "line must not be only whitespace"
    assert text.count(".") == 1, "entry must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    return text


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
