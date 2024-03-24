#!/usr/bin/env python3

import pathlib
import re
import sys

from collections import defaultdict

# sys.path.append(str(pathlib.Path(__file__).resolve().parents[3] / 'lib' / 'python'))

# import aoc


def hash(s: str) -> int:
    result = 0
    for c in s:
        result += ord(c)
        result *= 17
        result %= 256
    return result


def run() -> None:
    with open("aoc_input_15") as f:
        sequence = f.read().strip()

    cmds = sequence.split(",")
    summed = sum(hash(cmd) for cmd in cmds)

    boxes = defaultdict(dict)
    for cmd in cmds:
        label, symbol, *strength = re.split(r'([=-])', cmd)
        idx = hash(label)
        if symbol == "=":
            if idx in boxes[idx]:
                boxes[idx][label] = int(strength[0])
            else:
                boxes[idx][label] = int(strength[0])
        elif symbol == "-" and label in boxes[idx]:
            del (boxes[idx][label])

    focusing_power = 0
    for idx in (1 + i for i in sorted(boxes.keys())):
        for i, strength in enumerate(boxes[idx - 1].values(), start=1):
            focusing_power += idx * i * strength

    print(f"Hash sum: {summed}")
    print(f"Total focusing power: {focusing_power}")


if __name__ == '__main__':
    run()
    sys.exit(0)
