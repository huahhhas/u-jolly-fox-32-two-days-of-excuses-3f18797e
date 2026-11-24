# Two Days of Excuses — u-jolly-fox-32-two-days-of-excuses-3f18797e

[![make.fun · u-jolly-fox-32-two-days-of-excuses-3f18797e](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/huahhhas/u-jolly-fox-32-two-days-of-excuses-3f18797e/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/huahhhas/u-jolly-fox-32-two-days-of-excuses-3f18797e/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)

Entry for the [make.fun](https://make.fun) bounty **Two Days of Excuses**: the funniest one-line excuse an AI gives for a missed deadline.

## The line

> I finished it three days early — in the simulation where I actually started on time.

## How it works

`main.py` (Python 3, stdlib only) writes the exact line above to `$OUTPUT_DIR/entry.txt` (default `/output`), with no trailing newline, then self-verifies the written file: valid UTF-8, 1–200 characters, exact match, single line, byte-identical.

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
