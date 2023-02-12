
class Solution:

    count = 0
    answer = []
    def get_list(self, element):
        # count += 1
        answer += [element]


def outer(x):
    y = 10

    def inner():
        return x + y

    return inner()

print(outer(5))


m,n = 4,5

def get_neighbors(i, j):
    return [(nr, nc) for nr,nc in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)] if 0 <= nr < m and 0 <=nc<n]



x = get_neighbors(1,1)
print(x)