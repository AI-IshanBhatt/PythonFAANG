from collections import deque


def create_graph(n):
    return [[] for _ in range(n)]


def add_edge(g,u,v):
    g[u].append(v)
    g[v].append(u)


def check_bipartition(g):
    colors = [0] * len(g)
    visited = [False] * len(g)

    def dfs(current, parent, current_color):
        if parent == -1:
            colors[current] = current_color
            visited[current] = True
            for node in g[current]:
                if not dfs(node, current, current_color*-1):
                    return False
        else:
            if not visited[current]:
                colors[current] = current_color
                visited[current] = True
                for node in g[current]:
                    if node != parent:
                        if not dfs(node, current, current_color*-1):
                            return False
            else:
                if colors[current] == colors[parent]:
                    return False
        return True

    def bfs(start_point):
        queue = deque()
        queue.append(start_point)
        current_color = 1

        while queue:
            for i in range(len(queue)):
                current = queue.popleft()
                if not visited[current]:
                    visited[current] = True
                    colors[current] = current_color
                    queue.extend(g[current])
                else:
                    if colors[current] == -1*current_color:
                        return False
            current_color *= -1

        return True

    def better_bfs(start_point):
        queue = deque([start_point])
        parent = -1
        colors[start_point] = 1

        while queue:
            current = queue.popleft()
            for i in g[current]:
                if i != parent:
                    if colors[i] == 0:  # No need for extra visited colors can be used to track visited node,
                        # See if it cn work for dfs as well
                        colors[i] = -1*colors[current]
                        queue.append(i)
                    else:
                        if colors[i] == colors[current]:
                            return False
            parent = current
        return True

    return better_bfs(0)


g = create_graph(5)
add_edge(g, 0, 1)
add_edge(g, 1, 2)
add_edge(g, 1, 3)
add_edge(g, 2, 4)
add_edge(g, 3, 4)
# add_edge(g, 0, 3)
# print(check_bipartition(g))
print(check_bipartition(g))

"""
Pattern Learned about when to return and when to continue in recursive function
Also check in detect_cycle_directed(), detect_cycle_undirected() as well as dfs here.
A big note will be prepared for this
"""