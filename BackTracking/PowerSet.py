from pprint import pprint


def get_powerset(nums):
    answer = []

    def dfs(start_point, temp):
        answer.append(temp)
        for i in range(start_point, len(nums)):
            dfs(i+1, temp+[nums[i]])
    dfs(0, [])
    return answer


pprint(sorted(get_powerset([1, 2, 3])))

