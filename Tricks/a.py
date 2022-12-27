from collections import defaultdict, deque


def find_diff(element, array):
    low = 0
    high = len(array) - 1
    min_diff = float('inf')
    ele2 = 0

    while low <= high:
        mid = (low+high) // 2

        if element == array[mid]:
            return element, 0
        if abs(element - array[mid]) < min_diff:
            min_diff = abs(element - array[mid])
            ele2 = array[mid]
        if element > array[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return ele2, min_diff



# print(find_diff(30, [15,17,26,134,135]))

def find_city_order(tuples):
    graph = defaultdict(int)
    adj_list = defaultdict(list)
    nodes = set()

    for u, v in tuples:
        nodes.add(u)
        nodes.add(v)
        graph[v] += 1
        adj_list[u].append(v)

    q = deque()
    for node in nodes:
        if graph[node] == 0:
            q.append(node)

    while q:
        current = q.popleft()
        print(current, end=" ")

        for node in adj_list[current]:
            graph[node] -= 1
            if graph[node] == 0:
                q.append(node)


find_city_order([("c","b"), ("d","c"), ("b","e"), ("a","d")])
print()
find_city_order([("A", "C"), ("B", "D"), ("C", "B")])



