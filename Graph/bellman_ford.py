import sys

# Best suited when graph is given as list of edges
# As this is what we want to traverse anyway


def create_graph(n):
    return [[] for _ in range(n)]


def add_edge(g, u, v, w):
    g[u].append((v, w))


def bellman_ford(g, start=0):
    answer = [sys.maxsize] * len(g)
    answer[start] = 0 # This is the only use of start, to specify distance=0
    edges = []
    for i in range(len(g)):
        for v,w in g[i]:
            edges.append((i,v,w))

    # For each iteration run each edges
    for _ in range(len(g)-1):
        for u,v,w in edges:
            answer[v] = min(answer[v], w + answer[u])

    print(answer)


if __name__ == "__main__":
    graph = create_graph(5)
    add_edge(graph, 0, 1, -1)
    add_edge(graph, 0, 2, 4)
    add_edge(graph, 1, 2, 3)
    add_edge(graph, 1, 3, 2)
    add_edge(graph, 1, 4, 2)
    add_edge(graph, 3, 2, 5)
    add_edge(graph, 3, 1, 1)
    add_edge(graph, 4, 3, -3)

    bellman_ford(graph)