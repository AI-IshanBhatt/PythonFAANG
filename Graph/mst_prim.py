import heapq


# The time complexity of Prim’s algorithm can be reduced to O(E * logV) with the help of a binary heap.


def create_graph(n):
    return [[] for _ in range(n)]


def add_weighted_edge(g, u,v,w):
    g[u].append((u, v, w))
    g[v].append((v, u, w))


def prim(g, start_point=0):
    edges = []
    visited = [False] * len(g)
    visited[start_point] = True
    mst_path = []
    mst_cost = 0

    for edge in g[start_point]:
        heapq.heappush(edges, edge[::-1])

    while edges:
        current_edge = heapq.heappop(edges)
        current_cost = current_edge[0]
        current_neighbor = current_edge[1]
        current_node = current_edge[2]

        if not visited[current_neighbor]:
            visited[current_neighbor] = True
            mst_cost += current_cost
            mst_path.append((current_node, current_neighbor))
            [heapq.heappush(edges, edge[::-1]) for edge in g[current_neighbor]]

    print(f"TOTAL COST {mst_cost}")
    print(f"MST PATH {mst_path}")


def prim_cool(g, start_point=0):
    total_cost = 0
    heap = [(0, start_point)]
    visited = [False] * len(g)

    while heap:
        cost, u = heapq.heappop(heap)
        if not visited[u]:
            total_cost += cost
            visited[u] = True

            for _, v, w in g[u]:
                if not visited[v]:
                    heapq.heappush(heap, (w, v))

    print(f"TOTAL COST {total_cost}")



if __name__ == "__main__":
    graph = create_graph(9)
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

    # graph = create_graph(3)
    # add_weighted_edge(graph, 0, 1, 1)
    # add_weighted_edge(graph, 0, 2, 9)
    # add_weighted_edge(graph, 1, 2, 3)

    prim(graph, 0)
    prim_cool(graph, 0)
    print()

    graph_f_c_c = create_graph(7)
    add_weighted_edge(graph_f_c_c, 0, 1, 2)
    add_weighted_edge(graph_f_c_c, 0, 2, 6)
    add_weighted_edge(graph_f_c_c, 1, 3, 5)
    add_weighted_edge(graph_f_c_c, 2, 3, 8)
    add_weighted_edge(graph_f_c_c, 3, 4, 10)
    add_weighted_edge(graph_f_c_c, 3, 5, 15)
    add_weighted_edge(graph_f_c_c, 4, 5, 6)
    add_weighted_edge(graph_f_c_c, 4, 6, 2)
    add_weighted_edge(graph_f_c_c, 5, 6, 6)
    prim(graph_f_c_c, start_point=0)
    prim_cool(graph_f_c_c)