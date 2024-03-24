from collections import Counter


def generate_subarrays(arr):
    answer = [[ele] for ele in arr]

    for i in range(len(arr)):
        temp = [arr[i]]
        for j in range(i+1, len(arr)):
            temp += [arr[j]]
            answer += [temp.copy()]

    c = Counter()
    for x in answer:
        c.update(Counter(x))

    print(c)
    return answer


print(generate_subarrays([3,1,2,4]))
