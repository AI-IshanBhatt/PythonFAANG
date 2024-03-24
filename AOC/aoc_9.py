with open("aoc_input_9") as f:
    lines = [[int(i.strip()) for i in l.split()] for l in f]

    final_one = 0
    final_two = 0
    for l in lines:

        first_last = [(l[0], l[-1])]
        while len(set(l)) != 1:
            x = []
            for i in range(len(l) - 1):
                x.append(l[i + 1] - l[i])
            l = x
            first_last.append((l[0], l[-1]))

        # part 1
        xi = 0
        for i in range(len(first_last)):
            xi += first_last[i][-1]

        final_one += xi

        # part 2
        final = 0
        xi = 0
        for i in range(len(first_last)):
            xi += first_last[i][0] if i % 2 == 0 else -first_last[i][0]

        final_two += xi

    print(final_one)
    print(final_two)
