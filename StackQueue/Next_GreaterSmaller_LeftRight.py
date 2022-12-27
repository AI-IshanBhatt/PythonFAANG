from typing import List


def next_greater_right(nums: List[int]) -> List[int]:
    stack = [len(nums) - 1]

    answer = [-1] * len(nums)

    for i in range(len(nums)-2, -1,-1):
        while stack and nums[i] >= nums[stack[-1]]:
            stack.pop()

        answer[i] = nums[stack[-1]] if stack else -1
        stack.append(i)

    return answer


def next_greater_left(nums: List[int]) -> List[int]:
    stack = [0]
    answer = [-1] * len(nums)

    for i in range(1, len(nums)):
        while stack and nums[i] >= nums[stack[-1]]:
            stack.pop()

        answer[i] = nums[stack[-1]] if stack else -1
        stack.append(i)

    return answer


def next_smaller_right(nums: List[int]) -> List[int]:
    stack = [len(nums) - 1]

    answer = [-1] * len(nums)

    for i in range(len(nums) - 2, -1, -1):
        while stack and nums[i] <= nums[stack[-1]]:
            stack.pop()

        answer[i] = nums[stack[-1]] if stack else -1
        stack.append(i)

    return answer


def next_smaller_left(nums: List[int]) -> List[int]:
    stack = [0]
    answer = [-1] * len(nums)

    for i in range(1, len(nums)):
        while stack and nums[i] <= nums[stack[-1]]:
            stack.pop()

        answer[i] = nums[stack[-1]] if stack else -1
        stack.append(i)

    return answer


print(next_greater_right([13,7,6,12]))
print(next_greater_left([13,7,6,12]))

print(next_smaller_right([13,7,6,12]))
print(next_smaller_left([13,7,6,12]))