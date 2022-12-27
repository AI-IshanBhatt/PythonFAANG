from typing import List
from math import inf
from collections import defaultdict


def taskSchedulerII(tasks: List[int], space: int) -> int:
    d = defaultdict(lambda: float(-inf))
    timer = 0

    for task in tasks:
        timer = d[task] = max(d[task] + space, timer) + 1

    return timer

print(taskSchedulerII([5,8,8,5], 4))