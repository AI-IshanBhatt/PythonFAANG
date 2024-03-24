def create_graph(n):
    return [[] for _ in range(n)]


def add_edge(g, u, v, bidirectional=False):
    g[u].append(v)
    if bidirectional:
        g[v].append(u)


def detect_cycle_directed(g):

    path = set()
    visited = [False] * len(g)

    def dfs_util(node):
        if visited[node] and node in path:
            return True
        else:
            if not visited[node]:
                visited[node] = True
                path.add(node)

                for n in g[node]:
                    if dfs_util(n):
                        return True
                path.remove(node)

    # Done for disconnected components
    for i in range(len(g)):
        if not visited[i]:
            if dfs_util(i):
                return True

    return False


def detect_cycle_undirected(g):
    visited = [False] * len(g)
    parent = -1

    def dfs_util(node, parent):
        if not visited[node]:
            visited[node] = True

            for i in g[node]:
                if i != parent:
                    if dfs_util(i, node):
                        return True
        else:
            return True

    for i in range(len(g)):
        if not visited[i]:
            if dfs_util(i, parent):
                return True

    return False


if __name__ == "__main__":
    edges = [[0, 1], [0, 2], [2, 3], [1, 4], [3, 4], [4, 5], [5,3]]  # Last one makes it a cycle
    vertex_count = 7
    graph = create_graph(vertex_count)
    [add_edge(graph, u, v) for u, v in edges]
    # print("BFS")
    # print(bfs(graph, 0))
    print("DFS")
    print(detect_cycle_directed(graph))

    graph = create_graph(9)
    add_edge(graph, 0, 1)
    add_edge(graph, 1, 2)
    add_edge(graph, 2, 3)
    add_edge(graph, 3, 1)  # This is making it cyclic
    add_edge(graph, 2, 5)
    add_edge(graph, 5, 4)
    add_edge(graph, 6, 1)
    add_edge(graph, 6, 7)
    add_edge(graph, 8, 7)
    add_edge(graph, 8, 6)
    print(detect_cycle_directed(graph))

