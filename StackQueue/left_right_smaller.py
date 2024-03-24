

def increasing_queue(nums):
    right_smaller_elements = [-1] * len(nums)
    left_smaller_elements = [-1] * len(nums)

    stack = []

    for i in range(len(nums)):
        while stack and nums[i] < nums[stack[-1]]:
            right_smaller_elements[stack.pop()] = nums[i]

        if stack:
            left_smaller_elements[i] = nums[stack[-1]]   # I could not knock it off

        stack.append(i)

    print(stack)
    print(left_smaller_elements)
    print(right_smaller_elements)


increasing_queue([5,3,1,2,4])