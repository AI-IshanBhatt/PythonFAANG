from collections import deque


def create_graph(n):
    return [[] for _ in range(n)]


def add_edge(g, u, v, bidirectional=False):
    g[u].append(v)
    if bidirectional:
        g[v].append(u)


def dfs(g, start_point):
    stack = [start_point]
    visited = [False] * len(g)

    while stack:
        current = stack.pop()
        if not visited[current]:
            print(current, end=" ")
            visited[current] = True
            stack.extend(g[current])


def dfs_recurse(g, start_point):
    answer = []
    visited = [False] * len(g)

    def dfs_util(current):
        visited[current] = True
        answer.append(current)

        for i in g[current]:
            if not visited[i]:
                dfs_util(i)

    dfs_util(start_point)
    return answer


def bfs(g, start_point):
    queue = deque([start_point])
    visited = [False] * len(g)

    while queue:
        current = queue.popleft()
        if not visited[current]:
            print(current, end=" ")
            visited[current] = True
            queue.extend(g[current])


def detect_cycle_directed(g):
    path, visited = set(), [False] * len(g)

    def detect_cycle_util(current):
        path.add(current)
        visited[current] = True

        for ele in g[current]:
            if visited[ele]:
                if ele in path:
                    return True
            else:
                if detect_cycle_util(ele):  # Can not return directly we only want to return if it is True in case of
                    # False we want to continue the loop, in case of True we do not want to check for anything else
                    return True
        path.remove(current)
        return False

    # Done for disconnected components
    for i in range(0, len(g)):
        if not visited[i]:
            if detect_cycle_util(i):
                return True
    return False


def detect_cycle_undirected(g):
    visited = [False] * len(g)

    def detect_cycle_util(current, parent):
        if visited[current]:
            return True
        else:
            visited[current] = True
            for node in g[current]:
                if node != parent:
                    if detect_cycle_util(node, current):  # Same if false we want to continue , Verified by debugger
                        return True
        return False

    for i in range(0, len(g)):
        if not visited[i]:
            if detect_cycle_util(i, -1):
                return True
    return False


graph = create_graph(9)
add_edge(graph, 0, 1)
add_edge(graph, 1, 2)
add_edge(graph, 2, 3)
add_edge(graph, 3, 4)
add_edge(graph, 2, 5)
add_edge(graph, 5, 4)
add_edge(graph, 6, 1)
add_edge(graph, 6, 7)
add_edge(graph, 8, 7)
add_edge(graph, 8, 6)

print(detect_cycle_directed(graph))
dfs(graph, 0)
print()
print(dfs_recurse(graph, 0))
print("+" * 100)

graph_1 = create_graph(7)
add_edge(graph_1, 0, 1, True)
add_edge(graph_1, 0, 2, True)
add_edge(graph_1, 2, 6, True)
add_edge(graph_1, 2, 3, True)
add_edge(graph_1, 3, 4, True)
add_edge(graph_1, 3, 5, True)
add_edge(graph_1, 0, 5, True)
dfs(graph_1, 0)
print()
print(dfs_recurse(graph_1, 0))
bfs(graph_1, 0)
print()
print(detect_cycle_undirected(graph_1))
