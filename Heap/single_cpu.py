from typing import List
import heapq


def getOrder(tasks: List[List[int]]) -> List[int]:
    tasks = sorted([(ele[0], ele[1], idx) for idx, ele in enumerate(tasks)])
    answer = []
    heap = []
    timer = tasks[0][0]
    idx = 0  # to know how many elements are processed

    while len(answer) < len(tasks):

        if heap and heap[0][2] <= timer:
            p_t, i, e_t = heapq.heappop(heap)
            answer.append(i)
            timer += p_t

        if idx < len(tasks) and tasks[idx][0] <= timer:
            while idx < len(tasks) and tasks[idx][0] <= timer:
                heapq.heappush(heap, (tasks[idx][1], tasks[idx][2], tasks[idx][0]))
                idx += 1

        elif idx < len(tasks) and tasks[idx][0] > timer:
            heapq.heappush(heap, (tasks[idx][1], tasks[idx][2], tasks[idx][0]))
            idx += 1
            timer = tasks[idx][0]  # Remember why there was max in for loop solution

    return answer


# x = getOrder([[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]])
x = getOrder([[5,2],[7,2],[9,4],[6,3],[5,10],[1,1]])
# x = getOrder([[1,2],[2,4],[3,2],[4,1]])
print(x)