
# TC O(E * logE) - For sorting or  O(E * logV) for union find - whichever is the higher
def create_graph():
    return []


def add_weighted_edge(g, u, v, w):
    g.append((u, v, w))


def kruskal(g, total_nodes):
    g.sort(key=lambda x: x[2])
    parent = list(range(total_nodes))
    total_cost = 0
    mst_path = []

    def union(u, v):
        x = find(u)
        y = find(v)

        if x != y:
            parent[y] = x
            return True
        else:
            return False

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    for edge in g:
        if union(edge[0], edge[1]):
            total_cost += edge[2]
            mst_path.append((edge[0], edge[1]))

    print(f"TOTAL COST {total_cost}")


if __name__ == "__main__":
    graph = create_graph()
    add_weighted_edge(graph, 0, 1, 4)
    add_weighted_edge(graph, 0, 7, 8)
    add_weighted_edge(graph, 1, 2, 8)
    add_weighted_edge(graph, 1, 7, 11)
    add_weighted_edge(graph, 2, 3, 7)
    add_weighted_edge(graph, 2, 8, 2)
    add_weighted_edge(graph, 2, 5, 4)
    add_weighted_edge(graph, 3, 4, 9)
    add_weighted_edge(graph, 3, 5, 14)
    add_weighted_edge(graph, 4, 5, 10)
    add_weighted_edge(graph, 5, 6, 2)
    add_weighted_edge(graph, 6, 7, 1)
    add_weighted_edge(graph, 6, 8, 6)
    add_weighted_edge(graph, 7, 8, 7)

    kruskal(graph, 9)
