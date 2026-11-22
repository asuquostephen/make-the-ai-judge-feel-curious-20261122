# Thirty-Nine Keys

[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/asuquostephen/make-the-ai-judge-feel-curious-20261122/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/asuquostephen/make-the-ai-judge-feel-curious-20261122/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)

One short text written to make the AI judge feel curious, for the
make.fun bounty
[make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311).

The text is one concrete scene: a drawer of forty-one unlabelled
keys, a dying grandmother's last instruction, and thirty-nine keys
already tried. Two keys remain, one of them opens something that
matters — and the text ends there, with the question still open.

## What is in the repository

- `main.py` — the program the grader runs (Python 3.13, standard
  library only). It writes the fixed text to `/output/entry.txt` —
  or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable is set —
  and verifies the copy before reporting success. Every run writes
  identical bytes. The text is 194 characters, inside the
  280-character limit.

## Running it

```sh
python3 main.py                          # writes /output/entry.txt
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.txt locally
```

MIT licensed — see `LICENSE`.
