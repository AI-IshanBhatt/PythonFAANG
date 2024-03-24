from collections import deque


def create_graph(n):
    return [[] for _ in range(n)]


def add_edge(g, u, v):
    g[u].append(v)
    g[v].append(u)


def bfs(g, start_point):

    queue = deque([start_point])
    visited = [False] * len(g)
    answer = []
    parent = -1

    while queue:
        current = queue.popleft()

        if not visited[current]:
            visited[current] = True
            answer.append(current)
            [queue.append(v) for v in g[current] if v != parent]
            parent = current

    return answer


def dfs(g, start_point):

    visited = [False] * len(g)
    answer = []

    def dfs_util(node, parent):
        if not visited[node]:
            answer.append(node)
            visited[node] = True

            [dfs_util(i, node) for i in g[node] if i != parent]

    dfs_util(start_point, -1)
    return answer


if __name__ == "__main__":
    edges = [[0, 1], [0, 2], [2, 3], [1, 4], [3, 4], [4, 5]]
    vertex_count = 6
    graph = create_graph(vertex_count)
    [add_edge(graph, u, v) for u, v in edges]
    # print("BFS")
    # print(bfs(graph, 0))
    print("DFS")
    print(dfs(graph, 0))

    edges = [[0, 1], [0, 2], [0, 3], [1, 3], [1, 5], [2, 4], [3, 5], [4, 6], [5, 6]]
    vertex_count = 7
    graph = create_graph(vertex_count)
    [add_edge(graph, u, v) for u, v in edges]
    # print("BFS")
    # print(bfs(graph, 0))
    print("DFS")
    print(dfs(graph, 0))