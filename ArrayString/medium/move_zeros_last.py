def move_zeros_last(nums):
    count = 0
    for idx, ele in enumerate(nums):
        if ele != 0:
            nums[idx], nums[count] = nums[count], nums[idx]
            count += 1

    return nums

nums = [1, 2, 3, 0, 4, 0, 6]
print(move_zeros_last(nums))