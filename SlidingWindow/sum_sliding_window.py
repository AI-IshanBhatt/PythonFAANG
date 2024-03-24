import math


def sum_sliding_window_basic(array, k):

    current_sum = sum(array[:k])
    answer = [current_sum]

    for i in range(k, len(array)):
        current_sum += (array[i] - array[i-k])
        answer.append(current_sum)

    return answer


def sum_sliding_window_two_pointers(array, k):

    l, r = 0, k
    first_sum = sum(array[:k])
    answer = [first_sum]

    while r < len(array):
        first_sum += (array[r] - array[l])
        answer.append(first_sum)
        l, r = l+1, r+1

    return answer


def max_difference_in_the_window(array, k):
    # Here we will not pre-calculate anything, and we try to run array like 123,234,345,456 ....
    # This is useful for situations where we do not have to sum/product k elements in one go.
    # We are not pre-computing anything, this will turn into above variant if we need to traverse the array.
    # Here we keep on tracking some condition between first and last element if the window.
    min_diff = math.inf

    for i in range(len(array) -k +1):
        min_diff = min(min_diff, array[i+k-1] - array[i])

    return min_diff




print(sum_sliding_window_basic([1,2,3,4,5,6,7], 3))
print(sum_sliding_window_two_pointers([1,2,3,4,5,6,7], 3))

print(max_difference_in_the_window([3,5,9,12,18,20,21], 3))