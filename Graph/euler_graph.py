# THis is applicable only to undirected graphs
# In Undirected graphs, sum of all degree is even
# That's because for a single edge to exists it will have 1 incoming degree to both of it;s vertex
# 1<-->2, Here 1 and 2 both have 1 degree so total is 2, so there can never be odd number of vertex having odd degree
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


def exists_euler_circuit(g):
    incoming_edges = [0] * len(g)

    for i in range(len(g)):
        for n in g[i]:
            incoming_edges[n] += 1

    total_odd_edges = sum(1 for i in incoming_edges if i % 2 == 1)
    return True if total_odd_edges == 0 else False


if __name__ == "__main__":
    g1 = create_graph(5)
    add_edge(g1, 0, 2)
    add_edge(g1, 2, 1)
    add_edge(g1, 1, 0)
    add_edge(g1, 0, 3)
    add_edge(g1, 3, 4)
    print(f"PATH {exists_euler_path(g1)}")
    print(f"CYCLE {exists_euler_circuit(g1)}")

    g2 = create_graph(5)
    add_edge(g2, 1, 0)
    add_edge(g2, 0, 2)
    add_edge(g2, 2, 1)
    add_edge(g2, 0, 3)
    add_edge(g2, 3, 4)
    add_edge(g2, 4, 0)
    print(f"PATH {exists_euler_path(g2)}")
    print(f"CYCLE {exists_euler_circuit(g2)}")

    g3 = create_graph(5)
    add_edge(g3, 1, 0)
    add_edge(g3, 0, 2)
    add_edge(g3, 2, 1)
    add_edge(g3, 0, 3)
    add_edge(g3, 3, 4)
    add_edge(g3, 1, 3)
    print(f"PATH {exists_euler_path(g3)}")
    print(f"CYCLE {exists_euler_circuit(g3)}")

    # Let us create a graph with 3 vertices
    # connected in the form of cycle
    g4 = create_graph(3)
    add_edge(g4, 0, 1)
    add_edge(g4, 1, 2)
    add_edge(g4, 2, 0)
    print(f"PATH {exists_euler_path(g4)}")
    print(f"CYCLE {exists_euler_circuit(g4)}")

    # Let us create a graph with all vertices
    # with zero degree
    g5 = create_graph(3)
    print(f"PATH {exists_euler_path(g5)}")
    print(f"CYCLE {exists_euler_circuit(g5)}")


