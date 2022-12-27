from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    stack = [0]
    answer = [0] * len(temperatures)

    for i in range(1, len(temperatures) - 1):
        while stack and temperatures[i] >= temperatures[stack[-1]]:
            answer[stack.pop()] = i - stack[-1]

        stack.append(i)

    return answer


print(dailyTemperatures([73,74,75,71,69,72,76,73]))