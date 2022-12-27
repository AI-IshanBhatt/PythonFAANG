from typing import List


def findKthPositive(arr: List[int], k: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        missing = arr[mid] - (mid + 1)
        if missing >= k:
            right = mid - 1
        else:
            left = mid + 1

    print(left,right)
    return left + k


findKthPositive([2,9,12,13,15], 5)