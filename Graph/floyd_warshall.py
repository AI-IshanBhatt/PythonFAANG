# This is most suitable when graph as an adj matrix is given
# If not convert it into adj matrix
# Useful only with directed graph
import sys


def create_graph(n):
    g = [[sys.maxsize]*n for _ in range(n)]
    for i in range(n):
        g[i][i] = 0
    return g


def add_edge(g, u, v, w):
    g[u][v] = w


def floyd_warshall(g):
    for k in range(len(g)):
        for i in range(len(g)):
            for j in range(len(g)):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])


if __name__ == "__main__":
    graph = create_graph(4)
    print(graph)
    add_edge(graph, 0, 2, -2)
    add_edge(graph, 1, 0, 4)
    add_edge(graph, 1, 2, 3)
    add_edge(graph, 2, 3, 2)
    add_edge(graph, 3, 1, -1)

    floyd_warshall(graph)
    print(graph)


