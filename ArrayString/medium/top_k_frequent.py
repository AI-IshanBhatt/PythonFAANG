from typing import List
from collections import Counter, defaultdict


# Using frequency sort
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    c = Counter(nums)
    d = defaultdict(list)
    most_frequent = 0
    answer = []

    for ele,count in c.most_common():
        d[count] += [ele]
        most_frequent = max(most_frequent, count)

    # You do not want 0th time,
    # If you are banned from using counter
    for i in range(most_frequent,0,-1):
        answer.extend(d[i])
        if len(answer) > k:
            return answer[:k]

    return answer

def topKFrequentWithCounter(nums: List[int], k: int) -> List[int]:
    c = Counter(nums)
    size = 0
    answer = []

    for ele, _ in c.most_common():
        if size < k:
            answer.append(ele)
            size += 1
        else:
            break
    return answer

