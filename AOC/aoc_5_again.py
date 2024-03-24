from collections import defaultdict
from pprint import pprint
with open("aoc_input_5") as f:
    lines = [l.strip() for l in f.readlines()]

    seeds = [int(i.strip()) for i in lines[0].split(":")[1].split(" ") if i]

    seeds_corrected = []
    j = 0
    while j < len(seeds):
        seeds_corrected.extend(list(range(seeds[j], seeds[j]+seeds[j+1])))
        j += 2

    # print(seeds_corrected)

    map_heads = ["seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:", "water-to-light map:",
                 "light-to-temperature map:", "temperature-to-humidity map:", "humidity-to-location map:"
                 ]

    d = defaultdict(list)
    i = 1
    while i < len(lines):
        if lines[i].strip() in map_heads:
            head = lines[i]
            i += 1
            while i < len(lines) and lines[i].strip():
                start, end, r = [int(x.strip()) for x in lines[i].strip().split(" ") if x != ""]
                d[head].append((end, end+r, start, r))
                i += 1
        i += 1

    print("dict collected")

    # for k,v in d.items():
    #     print(k,v)

    answer = 100000000000000000000000000009
    for s in seeds_corrected:
        for k, v in d.items():
            for item in v:
                if item[0] <= s < item[1]:
                    s = (s - item[0] + item[2])
                    break
        answer = min(answer, s)

    print(answer)