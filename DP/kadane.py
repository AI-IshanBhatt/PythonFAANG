import sys


def kadane(nums):
    curr_max = 0
    max_overall = -sys.maxsize
    start, start_dummy, end = 0, 0, 0

    for i in range(len(nums)):
        if nums[i] > curr_max + nums[i]:
            start_dummy = i
            curr_max = nums[i]
        else:
            curr_max = curr_max + nums[i]

        if curr_max > max_overall:
            max_overall = curr_max
            end = i

    print(start_dummy, end)
    return max_overall


nums = [-2, -3, 4, -1, -2, 1, 5, -3]
print(kadane(nums))
