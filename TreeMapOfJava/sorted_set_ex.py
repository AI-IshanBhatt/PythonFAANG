from sortedcontainers import SortedSet

ss = SortedSet(key=lambda x:-x)

ss.add(1)
ss.add(5)
ss.add(10)
ss.add(7)
ss.add(2)

ss.remove(7)
print(ss)

# Java implementation has floor and ceil on key, in python one you do not get the element back but you get index
# So you have to keep in mind
print(ss.bisect_right(7))

# ss.add(-1)
print(ss[2])

# Important operations would be
# add, remove, 0th element, bisect_left, bisect_right -> they return index instead of element

print(ss.pop())  # It removed the largest/smallest element from the list
print(ss)

print(ss.bisect_key_left(5))
print("===================================================================================================")

ss1 = SortedSet()
ss1.add(10)
ss1.add(15)
ss1.add(77)
ss1.add(4)
ss1.add(1)
print(ss1.bisect_left(4))
print(ss1.bisect_right(4))