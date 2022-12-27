
def combination_sum2(candidates, target):
    answer = []
    candidates.sort()

    def dfs(start_point, temp, current_sum):
        if current_sum == target:
            answer.append(temp)
        elif current_sum > target:
            return
        else:
            for i in range(start_point, len(candidates)):
                # This is very important, You want to consider the element for the first time
                # So we ignore the duplicates after the first element
                # In the 2nd level 1 will be considered as it is the 1st element at that level
                # In 1st level 1 will be 2nd element, so it should not be considered
                if i > start_point and candidates[i - 1] == candidates[i]:
                    continue
                else:
                    dfs(i + 1, temp + [candidates[i]], current_sum + candidates[i])

    dfs(0, [], 0)
    return answer


print(combination_sum2([1,1,2,2,2], 4))