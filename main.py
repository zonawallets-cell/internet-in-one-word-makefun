"""The Internet in One Word — make.fun entry.

Writes one word (at most 30 characters): the single word that best
describes the whole internet, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

Pure standard library only.

Why this word: the internet is feral — wild, untamed, no rules, no
owner, thriving on its own terms. It makes a reader laugh and then
nod: the whole internet in five letters, a word nobody's first reach
would be (not "chaos", not "memes", not "addiction"), yet true of the
internet as a whole rather than one app, one site or one mood. Short
enough to land in one beat, spelled correctly, instantly readable.
"""

import os

WORD = "feral"

MAX_CHARS = 30


def validate(text):
    """Enforce the RULES.txt gate: UTF-8, 1-30 chars, not only
    whitespace, a single word, and free of control characters."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text or text.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("entry must be at most %d characters" % MAX_CHARS)
    if any(ch.isspace() for ch in text):
        raise ValueError("entry must be a single word with no whitespace")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("entry must be free of control characters")
    text.encode("utf-8")
    return text


def main():
    validate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    # Re-validate the written file byte-for-byte: what the grader
    # reads must be exactly the validated word, nothing else.
    with open(path, "rb") as f:
        written = f.read()
    if written.decode("utf-8") != WORD:
        raise ValueError("written entry does not match the word")
    validate(written.decode("utf-8"))


if __name__ == "__main__":
    main()
