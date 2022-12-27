from pprint import pprint


def get_combinations(nums, k):
    answer = []

    def dfs(start_point, temp):
        if len(temp) == k:
            answer.append(temp)
        else:
            for i in range(start_point, len(nums)):
                dfs(i+1, temp+[nums[i]])

    dfs(0, [])
    return answer


pprint(get_combinations([1,2,3,4], 2))