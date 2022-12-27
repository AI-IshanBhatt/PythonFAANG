def search(nums, target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (high + low) // 2

        if nums[mid] == target:
            return mid
        elif nums[low] <= nums[mid]:  # Meaning no rotation on left side
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:  # Meaning no rotation on right side
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

print(search([4,5,6,7,0,1,2], 6))