# https://www.geeksforgeeks.org/chocolate-distribution-problem/

def get_min_diff(nums, k):
    nums.sort()

    min_diff = nums[k-1] - nums[0]

    for i in range(k, len(nums)):
        min_diff = min(min_diff, nums[i] - nums[i-k+1])

    return min_diff


print(get_min_diff([7, 3, 2, 4, 9, 12, 56], 3))