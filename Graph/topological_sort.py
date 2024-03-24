from collections import deque


def create_graph(n):
    return [[] for _ in range(n)]


def add_edge(g, u, v):
    g[u].append(v)


def topological_sort_bfs(g):
    in_degrees = [0] * len(g)
    answer = []
    total_visited = 0

    for node in g:
        for neighbor in node:
            in_degrees[neighbor] += 1

    queue = deque()
    [queue.append(i) for i in range(len(in_degrees)) if in_degrees[i] == 0]

    while queue:
        current = queue.popleft()

        answer.append(current)
        total_visited += 1

        for neighbor in g[current]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                queue.append(neighbor)

    print(total_visited == len(g))
    return answer


def topological_sort_dfs(g):
    visited = [False] * len(g)
    answer = []

    def dfs_util(start):
        visited[start] = True

        for neighbor in g[start]:
            if not visited[neighbor]:
                dfs_util(neighbor)

        # Add after your dfs is done
        answer.append(start)

    # Have to do it for all the elements
    for i in range(len(g)):
        if not visited[i]:
            dfs_util(i)

    return answer[::-1]  # Always use slicing, it is cool


if __name__ == "__main__":
    edges = [[5,0], [4,0], [5,2], [4,1], [2,3], [3,1], [0,3]]
    edges = [[0,2], [3,0], [1,4], [1,2], [4,2], [4,0], [2,3]]
    vertex_count = 5

    graph = create_graph(vertex_count)
    [add_edge(graph,u,v) for u,v in edges]

    print(topological_sort_bfs(graph))
    print(topological_sort_dfs(graph))