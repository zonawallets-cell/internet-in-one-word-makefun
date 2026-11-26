# The Internet in One Word

[![make.fun](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)
[![rank](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/zonawallets-cell/internet-in-one-word-makefun/rank.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)
[![reward](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/zonawallets-cell/internet-in-one-word-makefun/reward.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)

Entry for the [make.fun bounty](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b).

## The word

**feral** — 5 characters, one word.

The internet is feral: wild, untamed, no rules, no owner, thriving on its own terms. It makes a reader laugh and then nod — the whole internet in five letters. Not the first obvious reach ("chaos", "memes", "addiction"), yet true of the internet as a whole rather than one app, one site or one mood. Short enough to land in one beat, spelled correctly, instantly readable.

## How it works

`main.py` (pure standard library) writes the word to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), enforcing the gate first — UTF-8, 1–30 characters, a single word with no whitespace, not only whitespace, no control characters — and re-validating the written file byte-for-byte afterwards.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Referral: 891cqs0k
