from sortedcontainers import SortedDict


def merge(intervals):
    d = SortedDict()

    for i, j in intervals:
        d[i] = d.get(i, 0) + 1
        d[j] = d.get(j, 0) - 1

    total, start, end, answer = 0, 0, 0, []
    for k, v in d.items():
        total += v
        if v != 0 and total == 1:
            start = k

        if total == 0:
            end = k
            answer.append([start, end])