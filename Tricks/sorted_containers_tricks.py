"""
These structures are important where you are expected to use Java's TreeMap
That is sorted list or sorted map/dict based on Key
The difference between this and using sorted(d.items()) is
    1. Everytime you insert a k,v pair you would have to sort it again OR
    2. Use bisect module to determine insertion position
https://grantjenks.com/docs/sortedcontainers/introduction.html#sorted-list
https://grantjenks.com/docs/sortedcontainers/introduction.html#sorted-dict
"""
from sortedcontainers import SortedSet, SortedDict, SortedList

print("SORTED LIST")
sl = SortedList()
# Insertion also happens in O(logn)
sl.add(5)
sl.add(3)
sl.add(3)
sl.add(9)
sl.add(2)
print(sl)
# All below methods are O(logn) as underlying list is sorted.
print(sl.bisect_left(2))
print(sl.bisect_right(2))
print(sl.bisect_left(3))
print(sl.bisect_right(3))
print(sl.index(3))

print("SORTED DICT")
sd = SortedDict()
sd[3] = sd.get(3, 0) + 1
sd[11] = sd.get(11, 0) + 1
sd[15] = sd.get(15, 0) - 1
sd[7] = sd.get(7, 0) - 1
print(sd)

sl.clear()
sl.add(10)
sl.add(20)

# Need to implement bisect_left and bisect_right WHY ONE BISECT LEFT AND OTHER BISECT RIGHT ?
print(sl.bisect_right(4))
print(sl.bisect_left(10))



print("Bisecting on Dict ?")
# print(sd.bisect_key_right(3))
# print(sd.bisect_key_left(3))

print(sd.items()[0])


print("NEW Sorted Dict")
sd1 = SortedDict()
sd1[10] = 1
sd1[20] = -1

print(sd1.bisect_right(50))
print(sd1.bisect_left(60))