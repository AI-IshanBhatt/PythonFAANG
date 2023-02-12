from collections import Counter

# Sorting a lost based on Lexicographical String ordering
l = [1,100,0,2,5,22,19]
print(sorted(l))
print(sorted(l, key=lambda x: str(x)))


# Sorting a list based on frequency
l = [1,2,3,4,3,3,3,6,7,1,1,9,3,2]
counts = Counter(l)
print(sorted(l, key=lambda x:counts[x]))
print(sorted(l, key=l.count))  # Don't do that it will count for each element making whole operation O(n2)
print(sorted(l, key=lambda x:-counts[x]))  # Max frequency is first

print("Sorting by custom function")
def key_func(i):
    if i == 2:
        return -1
    else:
        return i

print(sorted(l, key=key_func))

# Whatever you use in sorting, it applies to max,min as well
l = [1,2,3,4,3,3,3,6,7,1,1,9,3,2]
print(f"Max occurring {max(l, key=l.count)}")
print(f"Min occurring {min(l, key=l.count)}")
print(f"Frequency of 3 {l.count(3)}")

# Doing it for the dict
d = {"a":10, "b":5, "d":7, "f":9, "e":15}
print("Getting min-max KEY ONLY")
print(min(d))
print(max(d))
print("Getting min-max KEY ONLY based on VALUE")
print("MIN")
print(min(d, key=lambda x:d[x]))
print(min(d, key=d.get))
print("MAX")
print(max(d, key=lambda x:d[x]))
print(max(d, key=d.get))

# You can not use d.get here as the things we are sorting is d.items() NOT d
print("Getting max Key-Value pair, min is self")
max_pair = max(d.items(), key=lambda x:x[1])  # Here we are sorting d.items() which is a list of tuples
print(max_pair)

print("Sorting by KEY-VALUE, Ascending Descending ONLY RETURNS KEYS")
print(sorted(d))  # Returns keys as list
print(sorted(d, key=d.get))
print(sorted(d, key=d.get, reverse=True))

print("Returning the whole dict back")
print(dict(sorted(d.items())))
print(dict(sorted(d.items(), key=lambda x:x[1])))
print(dict(sorted(d.items(), key=lambda x:x[1], reverse=True)))
print(dict(sorted(d.items(), key=lambda x:-x[1])))



