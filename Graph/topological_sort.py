from collections import deque


def create_graph(n):
    return [[] for _ in range(n)]


def add_edge(g,u,v):
    g[u].append(v)


def topological_order_kahn(g):
    incoming_degrees = [0] * len(g)
    topological_order = []
    q = deque()
    for edges in g:
        for edge in edges:
            incoming_degrees[edge] += 1

    for idx,ele in enumerate(incoming_degrees):
        if ele == 0:
            q.append(idx)

    while q:
        current = q.popleft()
        topological_order.append(current)
        for edge in g[current]:
            incoming_degrees[edge] -= 1
            if incoming_degrees[edge] == 0:
                q.append(edge)

    if any(incoming_degrees):
        print("Cycle Detected")

    return topological_order


# We push the root/starting node in the beginning at the end.
# Two variations of dfs

def topological_order_dfs(g):
    visited = [False] * len(g)
    answer = deque()

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
add_edge(graph, 0, 2)
add_edge(graph, 1, 2)
add_edge(graph, 1, 3)
add_edge(graph, 2, 4)
add_edge(graph, 3, 5)
add_edge(graph, 4, 5)
add_edge(graph, 5, 6)
add_edge(graph, 6, 3)  # This edge makes the cycle

print(graph)
print(topological_order_kahn(graph))
print(topological_order_dfs(graph))