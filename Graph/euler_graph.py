# THis is applicable only to undirected graphs
# In Undirected graphs, sum of all degree is even
# That's because for a single edge to exists it will have 1 incoming degree to both of it;s vertex
# 1<-->2, Here 1 and 2 both have 1 degree so total is 2, so there can never be odd number of vertex having odd degree
from collections import deque


def create_graph(n):
    return [[] for _ in range(n)]


def add_edge(g, u, v):
    g[u] += [v]
    g[v] += [u]


def exists_euler_path(g):
    incoming_edges = [0] * len(g)

    for i in range(len(g)):
        for neighbor in g[i]:
            incoming_edges[neighbor] += 1

    total_odd_edges = sum(1 for i in incoming_edges if i % 2 != 0)
    return False if total_odd_edges > 2 else True


def find_euler_path(g):
    degrees = [0] * len(g)
    visited_edges = set()  # Keep track of visited edges so you don't go back in visited edge
    for i in range(len(g)):
        for n in g[i]:
            degrees[n] += 1

    euler_path = deque()
    # start_point = degrees.index(min(degrees))

    def dfs_util(current, parent):
        if degrees[current] == 0:
            euler_path.appendleft(current)
            return

        for n in g[current]:
            if n != parent and degrees[n] > 0 and (current, n) not in visited_edges:
                degrees[current] -= 1
                degrees[n] -= 1
                visited_edges.add((n, current))
                visited_edges.add((current, n))
                dfs_util(n, current)

        if degrees[current] == 0:
            euler_path.appendleft(current)  # It is kept for directed graphs

    dfs_util(0, -1)
    return edgify(euler_path)


def edgify(euler_path):
    return [(euler_path[i], euler_path[i+1]) for i in range(len(euler_path)-1)]


def exists_euler_circuit(g):
    incoming_edges = [0] * len(g)

    for i in range(len(g)):
        for n in g[i]:
            incoming_edges[n] += 1

    total_odd_edges = sum(1 for i in incoming_edges if i % 2 == 1)
    return True if total_odd_edges == 0 else False


if __name__ == "__main__":
    # g1 = create_graph(4)
    # add_edge(g1, 0, 1)
    # add_edge(g1, 1, 2)
    # add_edge(g1, 0, 2)
    # add_edge(g1, 2, 3)
    # print(exists_euler_path(g1))
    # print(find_euler_path(g1))

    g2 = create_graph(6)
    add_edge(g2, 0, 1)
    add_edge(g2, 0, 3)
    add_edge(g2, 1, 2)
    add_edge(g2, 1, 4)
    add_edge(g2, 1, 5)
    add_edge(g2, 2, 3)
    add_edge(g2, 2, 4)
    add_edge(g2, 2, 5)
    print(find_euler_path(g2))

    # Adding 7,8 makes something wrong
    g3 = create_graph(9)
    add_edge(g3, 0, 1)
    add_edge(g3, 0, 4)
    add_edge(g3, 1, 2)
    add_edge(g3, 1, 3)
    add_edge(g3, 2, 3)
    add_edge(g3, 1, 4)
    add_edge(g3, 4, 5)
    add_edge(g3, 4, 6)
    add_edge(g3, 5, 6)
    add_edge(g3, 0, 7)
    add_edge(g3, 0, 8)
    add_edge(g3, 7, 8)
    print(find_euler_path(g3))


