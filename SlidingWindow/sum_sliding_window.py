def sum_sliding_window(array, k):

    current_sum = sum(array[:k])
    answer = [current_sum]

    for i in range(k, len(array)):
        current_sum += (array[i] - array[i-k])
        answer.append(current_sum)

    return answer


print(sum_sliding_window([1,2,3,4,5,6,7], 3))