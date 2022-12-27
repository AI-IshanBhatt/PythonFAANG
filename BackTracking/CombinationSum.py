def get_combination_sums(candidates, target):
    answer = []

    def dfs(start_point, temp, current_sum):
        if current_sum == target:
            answer.append(temp)
        elif current_sum > target:
            return
        else:
            for i in range(start_point, len(candidates)):
                dfs(i, temp+[candidates[i]], current_sum+candidates[i])

    dfs(0, [], 0)
    return answer


print(get_combination_sums([2, 3, 5], 8))
