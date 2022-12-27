import heapq
from collections import defaultdict

data = [3, 2, 5, 4]

heapq.heapify(data)
print(data)  # The order may not be sorted but 0th element is the lowest
print(heapq.heappop(data))
print(data)
heapq.heappush(data, 1)
heapq.heappush(data, 10)
print(data)
print()

print("MAX HEAP")
data = []
heapq.heapify(data)
heapq.heappush(data, -1 * 5)  # Explicitly multiply with -1
heapq.heappush(data, -1 * 9)
heapq.heappush(data, -1 * 2)
heapq.heappush(data, -1 * 8)
# print(-heapq.heappop(data))
# print(-heapq.heappop(data))

print("DOING k largest k smallest operations in list of size n with time complexity O(n + k log n)")
n_large = [-x for x in heapq.nlargest(2, data, key=lambda x: -x)]
print(n_large)
n_small = [-x for x in heapq.nsmallest(2, data, key=lambda x: -x)]
print(n_small)

print("HEAPQ Operations on custom data, int[], tuple, k,v pair and also MAx Heap Operations")
print("Simple top k frequent elements")
print("The trick is to put the data as tuple and keep the first element of tuple as element that is being COMPARED ")

l = [1, 2, 2, 1, 3, 3, 4, 1, 2, 5, 6, 7]
freq_dict = defaultdict(int)

for ele in l:
    freq_dict[ele] += 1

items = []
for k, v in freq_dict.items():
    if len(items) == 3:
        heapq.heappushpop(items,(v, k))  # This is very nitty trick, when you reach threshold do pushandpop in same call
        # That is faster as well
    else:
        heapq.heappush(items, (v, k))

print(items)

print("K Closest Points to Origin")
l = [[3, 3], [5, -1], [-2, 4], [1, 1], [0, 3]]
distances = []

for x, y in l:
    cart_dist = -(x * x + y * y)
    if len(distances) == 2:
        heapq.heappushpop(distances, (cart_dist, x, y))
    else:
        heapq.heappush(distances, (cart_dist, x, y))

for data in distances:
    print(data[1], data[2])
