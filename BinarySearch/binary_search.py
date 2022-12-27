def binary_search_iterative(nums, element):

    low, high = 0, len(nums)-1
    while low <= high:
        mid = high - (high - low)//2
        if nums[mid] == element:
            return mid
        elif nums[mid] > element:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def binary_search_recursive(nums, element, low, high):
    if low > high:
        return -1
    else:
        mid = high - (high - low) // 2
        if nums[mid] == element:
            return mid
        elif nums[mid] > element:
            return binary_search_recursive(nums, element, low, mid-1)
        else:
            return binary_search_recursive(nums, element, mid+1, high)


ls = [1, 2, 4, 5, 6, 7, 9, 12, 13, 15, 17, 20]
print(binary_search_iterative([1,3], 2))
print(binary_search_recursive(ls, 30, 0, len(ls)-1))

