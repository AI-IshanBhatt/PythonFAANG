
from collections import defaultdict
from functools import reduce

d = {"red": 12, "green": 13, "blue": 14}

with open("aoc_input_2") as f:
    sum_ = 0
    for line in f:
        flag = True
        game, config = line.split(":")

        for x in config.split(";"):
            for single in x.split(","):
                count, color = single.strip().split(" ")
                if int(count) > d[color]:
                    flag = False

        sum_ += int(game.split(" ")[1]) if flag else 0
    print(sum_)

with open("aoc_input_2") as f:
    sum_ = 0
    for line in f:
        flag = True
        _, config = line.split(":")

        min_colors = defaultdict(int)
        total = 1
        for x in config.split(";"):
            for single in x.split(","):
                count, color = single.strip().split(" ")
                min_colors[color] = max(min_colors[color], int(count))

        sum_ += (reduce(lambda a, b: a*b, min_colors.values()))

    print(sum_)