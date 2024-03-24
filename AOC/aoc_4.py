from collections import defaultdict
# 9496801
# 9496801

# LESSON LEARNED - ALWAYS STRIP THE STRING AND ALWAYS CHECK FOR '' in case of collecting them
with open("aoc_input_4") as f:
    lines = [l.strip() for l in f.readlines()]

    sum_ = 0
    d = defaultdict(int)
    for l in lines:
        card_1, card_2 = l.strip().split(":")

        # print(card_1.split(" "))
        current_card = int(card_1.split(" ")[-1].strip())
        d[current_card] += 1
        win_card = set([i for i in card_2.split("|")[0].strip().split(" ") if i])
        my_card = set([i for i in card_2.split("|")[1].strip().split(" ") if i])

        win_card.

        x = len(win_card.intersection(my_card))
        if x:
            sum_ += (2**(x-1))
            print(x)
            for i in range(x):
                d[current_card+i+1] += d[current_card]

    print(sum_)
    print(sum(d.values()))

