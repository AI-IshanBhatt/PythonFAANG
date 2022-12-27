from typing import List

# The trick is to get the answer without using // operator
# Approach, use prefix product and suffix product
# Here Prefix and Suffix will not include current element, only elements before and after


def solve(nums: List[int]) -> List[int]:
    n, answer, suffix = len(nums), [1]*len(nums), 1

    for i in range(1, n):
        answer[i] = answer[i-1] * nums[i-1]

    # Here answer is prefix product
    for i in range(n-1,-1,-1):
        answer[i] *= suffix
        suffix *= nums[i]  # suffix result at i, would be used at i-1

    return answer

print(solve([5,1,4,2]))