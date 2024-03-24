from collections import Counter
from dataclasses import dataclass
from functools import cmp_to_key

order_dict = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":1,"Q":12,"K":13,"A":14}

ordering = [(5,), (4,1), (3,2), (3,1,1), (2,2,1), (2,1,1,1), (1,1,1,1,1)]

@dataclass
class Game:
    idx: int
    counter_order: tuple
    hand: str
    bid: int = 0

games = []

def get_j_adder(tuples: list[tuple], hand):
    if hand == "JJJJJ":
        return "J"
    x = set(t[1] for t in tuples)
    if len(x) == len(tuples):
        return tuples[0][0]

    else:
        most = tuples[0][1]
        cards = [t for t in tuples if t[1] == most]
        return max(cards, key=lambda x: order_dict[x[0]])[0]


with open("aoc_7_input") as f:
    c = 1
    for l in f:
        row = l.strip().split()
        hand, bid = row[0].strip(), int(row[1].strip())

        if "J" not in hand:
            cx = Counter(hand)
            x = tuple((i[1] for i in cx.most_common()))
        else:
            cx = Counter(hand)
            j_val = cx.pop("J")
            mc = cx.most_common()
            j_adder = get_j_adder(mc, hand)
            cx[j_adder] += j_val
            x = tuple((i[1] for i in cx.most_common()))

        games.append(
            Game(c, x, hand, bid)
        )
        c += 1

def ordering_function(g1, g2):
    if ordering.index(g1.counter_order) < ordering.index(g2.counter_order):
        return -1
    elif ordering.index(g1.counter_order) > ordering.index(g2.counter_order):
        return 1
    else:
        for i,j in zip(g1.hand, g2.hand):
            if order_dict[i] > order_dict[j]:
                return -1
            elif order_dict[i] < order_dict[j]:
                return 1


x = sorted(games, key=cmp_to_key(ordering_function), reverse=True)

sum_ = 0
for idx, g in enumerate(x, start=1):
    sum_ += (idx * g.bid)

print(sum_)