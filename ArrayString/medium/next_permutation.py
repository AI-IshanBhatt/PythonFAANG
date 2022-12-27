
def find_next_permutation(nums):

    for i in range(len(nums)-1, -1, -1):
        if i > 0 and nums[i-1] < nums[i]:
            mis_matched = i-1
            break
    else:
        mis_matched = 0

    for i in range(len(nums)-1, mis_matched-1, -1):
        if nums[i] > nums[mis_matched]:
            nums[i], nums[mis_matched] = nums[mis_matched], nums[i]
            nums[mis_matched+1:] = nums[mis_matched+1:][::-1]  # Reversing a part of list
            break

nums = [1,9,4,7,6,5]
find_next_permutation(nums)
print(nums)