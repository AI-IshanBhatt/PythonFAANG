from collections import deque


def create_graph(n):
    return [[] for _ in range(n)]


def add_edge(g,u,v):
    g[u].append(v)


def topological_order_kahn(g):
    incoming_edges = [0] * len(g)
    queue = deque()
    answer, visited = [], [False] * len(g)

    for node in range(len(g)):
        for neighbor in g[node]:
            incoming_edges[neighbor] += 1

    for idx, ele in enumerate(incoming_edges):
        if ele == 0:
            queue.append(idx)

    while queue:
        current = queue.popleft()
        answer.append(current)

        if not visited[current]:
            visited[current] = True
            for neighbor in g[current]:
                incoming_edges[neighbor] -= 1
                if incoming_edges[neighbor] == 0:
                    queue.append(neighbor)

    return answer
# We push the root/starting node in the beginning at the end.
# Two variations of dfs


def topological_order_dfs(g):
    visited = [False] * len(g)
    answer = deque()

    # Dump current node at last in the beginning
    def dfs_util(current):
        visited[current] = True
        for node in g[current]:
            if not visited[node]:
                dfs_util(node)
        answer.appendleft(current)

    for i in range(len(g)):
        if not visited[i]:
            dfs_util(i)

    return answer


graph = create_graph(7)
# add_edge(graph, 0, 2)
# add_edge(graph, 0, 3)
# add_edge(graph, 3, 1)
# add_edge(graph, 4, 2)
# add_edge(graph, 4, 1)
# add_edge(graph, 5, 0)
# add_edge(graph, 5, 2)
# add_edge(graph, 0, 2)
# add_edge(graph, 1, 2)
# add_edge(graph, 1, 3)
# add_edge(graph, 2, 4)
# add_edge(graph, 3, 5)
# add_edge(graph, 4, 5)
# add_edge(graph, 5, 6)
# add_edge(graph, 6, 3)  # This edge makes the cycle
add_edge(graph, 0, 1)
add_edge(graph, 0, 2)
add_edge(graph, 1, 4)
add_edge(graph, 2, 4)
add_edge(graph, 2, 3)
add_edge(graph, 4, 3)
add_edge(graph, 4, 6)
add_edge(graph, 3, 5)
add_edge(graph, 6, 5)

print(graph)
print(topological_order_kahn(graph))
# print(topological_order_dfs(graph))