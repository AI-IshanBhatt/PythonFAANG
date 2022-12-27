# https://leetcode.com/problems/maximum-subarray/


def maxSubArray(nums) -> int:
    current_max = nums[0]
    max_overall = nums[0]

    for ele in nums[1:]:
        current_max = max(ele, ele + current_max)
        max_overall = max(current_max, max_overall)
        current_max = max(0, current_max)

    return max_overall