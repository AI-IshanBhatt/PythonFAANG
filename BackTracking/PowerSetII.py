from pprint import pprint

# TODO You would need used boolean array only when you can not use start_point in back tracking
# i can be checked against start_point to see if that is first iteration meaning,
# first element of current recursion is being considered


def get_powerset(nums):
    answer = []
    nums.sort()

    def dfs(start_point, temp):
        answer.append(temp)

        for i in range(start_point, len(nums)):
            # If the current element is first in the iteration, we have to recurse OR
            # If the number is not same as previous number, recurse
            # if i == start_point or nums[i-1] != nums[i]:
            #     dfs(i + 1, temp + [nums[i]])
            if i > start_point and nums[i-1] == nums[i]:
                continue
            else:
                dfs(i+1, temp+[nums[i]])

    dfs(0, [])
    return answer


pprint(get_powerset([1,2,2]))