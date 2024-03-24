from collections import defaultdict


def get_prefix_sum(arr):
    answer = [0] * len(arr)
    answer_dict = {}
    answer_with_count = defaultdict(int)

    for i in range(len(arr)):
        if i > 0:
            answer[i] += (answer[i-1] + arr[i])
        else:
            answer[i] = arr[i]
        answer_dict[answer[i]] = i
        answer_with_count[answer[i]] += 1

    return answer, answer_dict, answer_with_count


answer, answer_dict, answer_with_count = get_prefix_sum([1,3,2,5,8,7,-4,-3])
print(answer)
print(answer_dict)
print(dict(answer_with_count))
