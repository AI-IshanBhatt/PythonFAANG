from sortedcontainers import SortedList

s = SortedList()

s.add((10,20))
# s.add((15,25))
s.add((20,30))

print(s.bisect_right((35,40)))