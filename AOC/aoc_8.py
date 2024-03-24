from math import lcm

directions = "01110110110110001110110011101000110101010101010111000110111010011101110111001110101110110111001001001110111011010100101101110111010101011010100011101010111011101110100011010101010001110110110101011101011101110111010111000110111011001011011011100011011011010111000101111"

d = {}

with open("aoc_input_8") as f:
    lines = [l.strip() for l in f.readlines()]

    # Part - 1
    for l in lines:
        x = l.split("=")
        start = x[0].strip()
        points = [p.strip() for p in x[1].strip().strip("(").strip(")").split(",")]

        d[start] = points

    counter = 0
    start = "AAA"
    while start != "ZZZ":
        current = d[start]
        start = current[int(directions[counter%len(directions)])]
        counter += 1

    print(counter)

    counter = 0
    start_nodes = [i for i in d.keys() if i.endswith("A")]

    answers = []
    # Part 2
    for start in start_nodes:
        counter = 0
        while not start.endswith("Z"):
            current = d[start]
            start = current[int(directions[counter % len(directions)])]
            counter += 1

        answers.append(counter)
    # FInd LCM of all the counters
    # print(counter)
    print(lcm(*answers))