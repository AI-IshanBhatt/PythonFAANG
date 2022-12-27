
def find_right_most_less_than_or_equal_target(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2

        if target < nums[mid]:
            right = mid
        else:
            left = mid + 1

    return left - 1 if nums[left-1] == target else -1


answer = find_right_most_less_than_or_equal_target([5,7,7,7,8,8,8,10,12], 7)
print(answer)

answer = find_right_most_less_than_or_equal_target([2,2], 2)
print(answer)