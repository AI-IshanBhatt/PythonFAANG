from collections import Counter
import math
import heapq


def reorg_string_counter(s):
    counter = Counter(s)
    mid_len = math.ceil(len(s) / 2)

    if counter.most_common(1)[0][1] > mid_len:
        return ""
    else:
        answer = []
        for i in range(len(s)):
            char, count = counter.most_common(1)[0]
            counter.pop(char)
            if i > 0 and answer[i-1] == char:
                char1, count1 = counter.most_common(1)[0]
                answer.append(char1)
                counter.pop(char1)
                if count1 > 1:
                    counter[char1] = count1-1
                counter[char] = count
            else:
                answer.append(char)
                counter[char] = count - 1
    return "".join(answer)


def reorg_string_heap(s):
    counter = Counter(s)
    items = []

    for k,v in counter.items():
        heapq.heappush(items, (-v,k))

    answer = []
    for i in range(len(s)):
        freq, char = heapq.heappop(items)
        if i > 0 and answer[i-1] == char:
            freq1, char1 = heapq.heappop(items)
            answer.append(char1)
            if -freq1 > 1:
                heapq.heappush(items, (freq1+1,char1))
            heapq.heappush(items, (freq, char))
        else:
            answer.append(char)
            if -freq > 1:
                heapq.heappush(items, (freq+1, char))
    return "".join(answer)


print(reorg_string_counter("aaaawoopqb"))
print(reorg_string_heap("aaaawoopqb"))