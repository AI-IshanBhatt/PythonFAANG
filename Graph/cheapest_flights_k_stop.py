import sys
from collections import deque
from typing import List
import heapq


def dfs_with_prune(n: int, flights: List[List[int]], src: int, dst: int, k: int):
    graph = [[] for _ in range(n)]

    for u, v, w in flights:
        graph[u].append((v, w))

    visited = [False] * n
    answer = sys.maxsize

    def dfs(start, current_level, current_cost):

        nonlocal answer
        if current_level == k + 1:
            if start != dst:
                return

        if start == dst:
            answer = min(answer, current_cost)
            return

        visited[start] = True
        for v, w in graph[start]:
            if not visited[v] and current_cost + w < answer:  # You did current_cost + w, so why were you doing answer[u] + w before ?
                dfs(v, current_level + 1, current_cost + w)
        visited[start] = False

    dfs(src, 0, 0)
    return -1 if answer == sys.maxsize else answer


def bfs_with_prune(n: int, flights: List[List[int]], src: int, dst: int, k: int):
    graph = [[] for _ in range(n)]

    for u, v, w in flights:
        graph[u].append((v, w))

    queue = deque()
    queue.append((src, 0))
    answer = [sys.maxsize] * n
    answer[src] = 0
    stops = 0

    while queue and stops <= k:
        for _ in range(len(queue)):
            node, cost = queue.popleft()

            for neighbor, weight in graph[node]:
                if cost + weight < answer[neighbor]:
                    answer[neighbor] = cost + weight
                    queue.append((neighbor, answer[neighbor]))

        stops += 1

    return -1 if answer[dst] == sys.maxsize else answer[dst]


def bellman_ford_a(n: int, flights: List[List[int]], src: int, dst: int, k: int):
    # You are given edges so for bellman ford you do not need to construct graph
    answer = [sys.maxsize] * n
    answer[src] = 0

    for i in range(k+1):
        temp_answer = answer.copy()  # So whatever you update in temp_answer doesn't modify anything in answer
        for u, v, w in flights:
            if answer[u] == sys.maxsize:
                continue
            if answer[u] + w < temp_answer[v]:
                temp_answer[v] = answer[u] + w
        answer = temp_answer

    return -1 if answer[dst] == sys.maxsize else answer[dst]


def dij_with_prune(n: int, flights: List[List[int]], src: int, dst: int, k: int):
    graph = [[] for _ in range(n)]

    for u, v, w in flights:
        graph[u].append((v, w))

    # level, cost, node
    heap = [(0, src, 0)]
    answer = [sys.maxsize] * n
    min_dist = sys.maxsize

    while heap:
        level, stop, cost = heapq.heappop(heap)

        if level <= k+1 and stop == dst:
            min_dist = min(min_dist, cost)

        if level == k+1:
            continue

        for v, w in graph[stop]:
            if cost + w < answer[v]:
                answer[v] = cost + w
                heapq.heappush(heap, (level+1, v, cost+w))

    return -1 if min_dist == sys.maxsize else min_dist


input_1 = [4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1]
input_2 = [3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1]
input_3 = [3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0]
input_4 = [4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0, 3, 1]
input_5 = [5, [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]], 2, 1, 1]
input_6 = [3, [[0,1,2],[1,2,1],[2,0,10]] ,1, 2, 1]
input_7 = [5, [[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]], 0, 4, 1]
input_8 = [7, [[0,3,7],[4,5,3],[6,4,8],[2,0,10],[6,5,6],[1,2,2],[2,5,9],[2,6,8],[3,6,3],[4,0,10],[4,6,8],[5,2,6],[1,4,3],[4,1,6],[0,5,10],[3,1,5],[4,3,1],[5,4,10],[0,1,6]], 2, 4, 1]
input_9 = [5, [[0,1,1],[0,2,5],[1,2,1],[2,3,1],[3,4,1]], 0, 4, 2]

print(dfs_with_prune(*input_9))
print(bfs_with_prune(*input_9))
print(dij_with_prune(*input_9))
print(bellman_ford_a(*input_9))