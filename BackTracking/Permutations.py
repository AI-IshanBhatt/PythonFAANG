from pprint import pprint


def get_permutations(nums):
    answer = []

    def dfs(temp):
        if len(temp) == len(nums):
            answer.append(temp)
            return
        for ele in nums:
            if ele not in temp:
                dfs(temp + [ele])

    dfs([])
    return answer


pprint(get_permutations([1, 2, 2]))
