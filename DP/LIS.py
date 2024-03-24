from collections import deque


def lis(nums):
    answer = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                answer[i] = max(answer[i], 1 + answer[j])

    return answer

def get_number_of_lis(nums):
    answer = [1] * len(nums)
    count = [1] * len(nums)
    # count is number of the longest subsequence that ends at i. Think of [1,3,2] and [1,3,2,5]

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                if answer[i] < answer[j]+1:
                    answer[i] = answer[j] + 1
                    count[i] = count[j]
                elif answer[i] == answer[j] + 1:
                    count[i] += count[j]

    max_len = max(answer)
    return sum(count[i] for i in range(len(nums)) if answer[i] == max_len)



def get_max_lis(nums):
    dp = lis(nums)
    answer = []
    index, lis_val = max(enumerate(dp), key=lambda x: x[1])
    queue = deque([(index, lis_val, nums[index], [], 0)])

    while queue:
        index, lis_val, ele, path, sum_ = queue.popleft()
        path += [ele]
        sum_ += ele

        if lis_val == 1:
            answer.append((path, sum_))
            continue

        for i in range(index, -1, -1):
            if dp[i] == lis_val - 1 and dp[i] < dp[index]:
                queue.append((i, lis_val-1, nums[i], path.copy(), sum_))

    return max(answer, key=lambda x: x[1])[0][::-1]


def get_all_lis(nums):
    dp = lis(nums)
    answer = []
    index, lis_val = max(enumerate(dp), key=lambda x: x[1])
    queue = deque([(index, lis_val, nums[index], [])])

    while queue:
        index, lis_val, ele, path = queue.popleft()
        path += [ele]

        if lis_val == 1:
            answer.append(path)
            continue

        for i in range(index, -1, -1):
            if dp[i] == lis_val - 1 and dp[i] < dp[index]:
                queue.append((i, lis_val - 1, nums[i], path.copy()))

    return [i[::-1] for i in answer]

# print(print_lis([1,3,2,5,4,7])
print(get_number_of_lis([1,3,2,5,4,7]))
print(get_all_lis([1,3,2,5,4,7]))
print(get_max_lis([1,3,2,5,4,7]))


print()
print(get_all_lis([10,22,9,33,21,50,41,60,80,1]))
print(get_max_lis([10,22,9,33,21,50,41,60,80,1]))
