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
rank = [0] * 8


def union(u, v):
    # TC would be O(HeightOfTree)
    # Sirf parent se nai hoga, you have to call find
    x = find(u)
    y = find(v)

    # Their group is different, make one as parent of other
    # Eventually it will reach at root, until a[i] != i
    if x != y:
        parent[y] = x


def union_with_rank(u, v):
    # You are flattening it out at the same time
    x = find_path_compression(u)
    y = find_path_compression(v)

    if x != y:
        if rank[x] > rank[y]:
            parent[y] = x
        elif rank[y] > rank[x]:
            parent[x] = y
        else:
            parent[y] = x
            rank[x] += 1


def find(u):
    # TC would be O(HeightOfTree)
    return u if parent[u] == u else find(parent[u])


def find_path_compression(u):
    # Before you return you change the parent of the all intermediate nodes in the path to parent
    # So, You are again flattening the tree. YOU WILL NOT HAVE IT Because of union by rank,
    # but suppose you have 0-1-2-3 so parents are 0,0,1,2 , now you call find(2) so it will go to 1 then 0
    # And while recursing you change the parent of all intermediate node to ROOT.
    # So 0-1-2-3 becomes 0-1,0-2,0-3 and this is still valid because we still do not care whose parent is who
    # Just if they belong to same group or not.
    if parent[u] != u:
        parent[u] = find(parent[u])
    # Because you are setting parent[u] to find(parent[u]), so you have to return parent[u], that works in both case
    # If you thought of returning u that only works when  parent[u] == u, it would not take above assignment in consider
    return parent[u]


def are_connected(u, v):
    return find_path_compression(u) == find_path_compression(v)


if __name__ == "__main__":
    union_with_rank(0, 1)
    union_with_rank(2, 7)
    union_with_rank(3, 6)
    union_with_rank(1, 4)
    # print(parent)  # Parent of 4 becomes 0 not 1, so it, more like 0-1|0-4 rather than 0-1-4
    # print(rank)
    print(are_connected(0, 2))  # Should print False
    union_with_rank(0, 7)
    print(are_connected(0, 2))  # Should print True
    print(parent)
    print(rank)
    # print(parent[7])  -> 2
    # print(find(7)) -> 0
    # Let's use find_path_compression in union_by_rank and print above stmts, both should be 0
    print(parent[7])
    print(find(7))



