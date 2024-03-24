from sortedcontainers import SortedDict

# sorts based on the keys
sd = SortedDict()

sd[1] = 1
sd[2] = 3
sd[5] = 4
sd[-1] = 1
sd[10] = 0

# print(sd)
# print(sd[0])

print(sd.popitem())  # This one removes the last k,v in dict just like removing last element of the list, And largest too
print(sd)

print("======================================================")
print(sd.bisect_left(3))  # THIS RETURNS INDEX IN THE DICT WHERE THE CURRENT KEY WOULD BE PLACED
print(sd.bisect_left(5))
print(sd.bisect_right(5))

# Use this one liner if you can not use defaultdict
sd[100] = sd.get(100, 0) + 1
print(sd)
sd[100] = sd.get(100, 0) + 1
print(sd)