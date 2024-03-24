from collections import deque


def create_graph(n):
    return [[] for _ in range(n)]


def add_edge(g, u, v):
    g[u].append(v)


def bfs(g, start_point):

    queue = deque([start_point])
    visited = [False] * len(g)

    while queue:
        current = queue.popleft()
        if not visited[current]:
            print(current, end=" ")
            visited[current] = True
            [queue.append(v) for v in g[current]]


def dfs(g, start_point):

    visited = [False] * len(g)

    def dfs_util(node):
        if not visited[node]:
            visited[node] = True
            print(node, end=" ")

            for i in g[node]:
                dfs_util(i)

    dfs_util(start_point)


def dfs_with_multiple_components(g):

    visited = [False] * len(g)

    def dfs_util(node):
        if not visited[node]:
            visited[node] = True
            print(node, end=" ")

            for i in g[node]:
                dfs_util(i)

    for i in range(len(g)):
        if not visited[i]:
            dfs_util(i)


if __name__ == "__main__":
    edges = [[0, 1], [0, 2], [2, 3], [1, 4], [3, 4], [4, 5]]
    vertex_count = 6
    graph = create_graph(vertex_count)
    [add_edge(graph, u, v) for u, v in edges]
    print("BFS")
    bfs(graph, 0)
    print()
    print("DFS")
    dfs(graph, 0)
    print()
    dfs_with_multiple_components(graph)
    print()
    print()

    edges = [[0,1], [0,2], [0,3], [1,3], [1,5], [2,4], [3,5], [4,6], [5,6]]
    vertex_count = 7
    graph = create_graph(vertex_count)
    [add_edge(graph, u, v) for u, v in edges]
    print("BFS")
    bfs(graph, 0)
    print()
    print("DFS")
    dfs(graph, 0)
    print()
    dfs_with_multiple_components(graph)
