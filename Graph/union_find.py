# Useful to find if two nodes are connected or not in given graph
# 1 way is to do dfs from a node and see if other node comes into it, then it is part of connected component.
# dfs can take many unnecessary nodes into it, thus making it inefficient.

# Think of that make_friend example of Anuj Bhaiya, make_friend is add_edge
# https://www.youtube.com/watch?v=Kptz-NVA2RE

# Rank would come later
# NOTE THAT - It works because we are never asked to find which ALL elements belongs to same group
# That would either make extra dict holding that and requires traversal,
# until a[i] != i, loop and then add i to dict[a[i]]
# NOTE THAT - This can be done by recursively updating the adj list


parent = list(range(8))


# find will eventually reach position where it's index is same as value, that's representative of group
def find(a):
    return a if parent[a] == a else find(parent[a])


def union(a, b):
    x = find(a)
    y = find(b)

    # Their group is different, make one as parent of other
    # Eventually it will reach at root, until a[i] != i
    if x != y:
        parent[y] = x


def in_same_group(a, b):
    return find(a) == find(b)


if __name__ == "__main__":
    union(0, 1)
    union(2, 7)
    union(3, 6)
    print(in_same_group(0, 2))
    union(0, 7)
    print(in_same_group(1, 7))
    print(parent)

