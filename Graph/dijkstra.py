import heapq
import sys

# Best suited with adj list
# If list of edges are given, convert it into adj list
# In Prim, we do not calculate anything we just dump list of edges based on the weight and reachability
# Here we calculate answer array


def create_graph(n):
    return [[] for _ in range(n)]


def add_edge(g, u, v, w):
    g[u].append((v, w))
    # g[v].append((u, w))


def dijkstra(g, start_point):
    visited = set()
    heap = [(0, start_point)]
    vertices = len(g)
    answer = [sys.maxsize] * vertices
    answer[start_point] = 0

    # heapq.heapify(heap)

    while heap:
        dist, u = heapq.heappop(heap)
        if u not in visited:
            visited.add(u)
            for v, w in g[u]:
                if dist + w < answer[v]:
                    answer[v] = dist + w
                    heapq.heappush(heap, (answer[v], v))

    print(len(visited))
    print(answer)


if __name__ == "__main__":
    graph_g_4_g = create_graph(9)
    add_edge(graph_g_4_g, 0, 1, 4)
    add_edge(graph_g_4_g, 0, 7, 8)
    add_edge(graph_g_4_g, 1, 2, 8)
    add_edge(graph_g_4_g, 1, 7, 11)
    add_edge(graph_g_4_g, 2, 3, 7)
    add_edge(graph_g_4_g, 2, 8, 2)
    add_edge(graph_g_4_g, 2, 5, 4)
    add_edge(graph_g_4_g, 3, 4, 9)
    add_edge(graph_g_4_g, 3, 5, 14)
    add_edge(graph_g_4_g, 4, 5, 10)
    add_edge(graph_g_4_g, 5, 6, 2)
    add_edge(graph_g_4_g, 6, 7, 1)
    add_edge(graph_g_4_g, 6, 8, 6)
    add_edge(graph_g_4_g, 7, 8, 7)
    dijkstra(graph_g_4_g, start_point=0)

    graph_f_c_c = create_graph(7)
    add_edge(graph_f_c_c, 0, 1, 2)
    add_edge(graph_f_c_c, 0, 2, 6)
    add_edge(graph_f_c_c, 1, 3, 5)
    add_edge(graph_f_c_c, 2, 3, 8)
    add_edge(graph_f_c_c, 3, 4, 10)
    add_edge(graph_f_c_c, 3, 5, 15)
    add_edge(graph_f_c_c, 4, 5, 6)
    add_edge(graph_f_c_c, 4, 6, 2)
    add_edge(graph_f_c_c, 5, 6, 6)
    dijkstra(graph_f_c_c, start_point=0)

    graph = create_graph(6)
    add_edge(graph, 0, 1, 6)
    add_edge(graph, 0, 2, 2)
    add_edge(graph, 2, 1, 1)
    add_edge(graph, 1, 3, 8)
    add_edge(graph, 2, 4, 15)
    add_edge(graph, 3, 5, 10)
    add_edge(graph, 4, 5, 1)
    dijkstra(graph, start_point=0)

