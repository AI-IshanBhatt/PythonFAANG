def findKthLargest(nums, k):

    def kthLargest(low, high, k):
        pivot_index = partition(nums, low, high)

        if pivot_index == k:
            return nums[pivot_index]
        elif pivot_index < k:
            return kthLargest(pivot_index+1, high, k)
        else:
            return kthLargest(low, pivot_index-1,k)

    return kthLargest(0, len(nums)-1, len(nums)-k)


def partition(nums, low, high):
    pivot = nums[high]
    i = low-1

    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i+1], nums[high] = nums[high], nums[i+1]
    return i+1

print(findKthLargest([3,2,1,5,6,4], 2))