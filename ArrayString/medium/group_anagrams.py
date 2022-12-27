from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            sorted_string = "".join(sorted(s))
            d[sorted_string] += [s]

        return d.values()
