def cyclic_sort(nums):
    i = 0

    while i < len(nums):
        correct_index = nums[i] - 1

        if nums[i] != nums[correct_index]:
            nums[correct_index], nums[i] = nums[i], nums[correct_index]
        else:
            i += 1
    return nums


print(cyclic_sort([4,3,2,7,8,2,3,1]))