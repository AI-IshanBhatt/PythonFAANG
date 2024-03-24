
# Mono decreasing stck will give you left/right greater element

def decreasing_stack(nums):

    left_greater_elements = [-1] * len(nums)
    right_greater_elements = [-1] * len(nums)
    stack = []

    # Always use index, it will help in problems like daily temperature, stock span etc
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            right_greater_elements[stack.pop()] = nums[i]

        if stack:
            left_greater_elements[i] = nums[stack[-1]]  # This is the element I could not knock off so it becomes mine
        stack.append(i)

    print(stack)
    print(left_greater_elements)
    print(right_greater_elements)


decreasing_stack([5,3,1,2,4])
