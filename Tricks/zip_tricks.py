numbers = [1,2,3]
letters = ["a", "b", "c"]

zipped = zip(numbers, letters)
print(list(zipped))

# Multiple iterables can be passed, String is an iterable too
zipped_multiple = zip(numbers, letters, "xyz")
# print(list(zipped_multiple))

print("Looping over them")
for i,j,k in zipped_multiple:
    print(f"i -> {i}, j -> {j}, k -> {k}")


print("UNZIPPING THE SEQUENCES")
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)
print(numbers)  # Both of them are tuples
print(letters)

print("CREATING DICT FROM ITERABLES")
d = dict(zip(numbers, letters))
print(d)

print("="*100)


def method(*l):
    print(l)
    print(type(l))  # This is a tuple


def kw_method(**kwargs):
    print(kwargs)
    print(type(kwargs))  # This is a dict


method(*[1,2,3,4])
method(1,2,3,4)

kw_method(a=1,b=2,c=3)
kw_method(**{"a":1, "b":2})  # Simply passing dict won't work