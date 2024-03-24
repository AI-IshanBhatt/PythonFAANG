from collections import defaultdict
from math import inf
from typing import List


def taskSchedulerII(tasks: List[int], space: int) -> int:
    d = defaultdict(lambda: float(-inf))
    timer = 0

    for task in tasks:
        timer = d[task] = max(d[task] + space, timer) + 1

    return timer

print(taskSchedulerII([5,8,8,5], 4))