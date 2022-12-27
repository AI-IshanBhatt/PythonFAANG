from pprint import pprint


def get_permutations(nums):
    answer = []
    used = [False]*len(nums)

    nums.sort()

    def dfs(temp):
        if len(temp) == len(nums):
            answer.append(temp)
        else:
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i-1] and used[i-1]):
                    continue
                else:
                    used[i] = True
                    dfs(temp+[nums[i]])
                    used[i] = False

    dfs([])
    return answer


pprint(get_permutations([1, 2, 2]))
