def find_lsb(n):
    lsb = 0
    while n % 2 == 0:
        lsb += 1
        n //= 2

    return 2 ** lsb


# Fenwick tree is a one indexed tree so we will not use 0th element
def make_fenwick_tree(arr):
    fenwick_tree = [0] + arr

    for i in range(1, len(fenwick_tree)):
        lsb = find_lsb(i)
        if i + lsb < len(fenwick_tree):
            fenwick_tree[i + lsb] += fenwick_tree[i]

    return fenwick_tree


def find_sum(fenwick_tree, n):
    answer = 0
    while n != 0:
        answer += fenwick_tree[n]
        n -= find_lsb(n)
    return answer


def query_fenwick_tree(fenwick_tree, left, right):
    right += 1
    # According to formula it is sum(0,7) - sum(0,2)
    # sum(0,2) according to Fenwick is 1,3 and left is anyway 3 so we do as it is
    # sum(0,7) according to Fenwick is 1,8, right is 7 so we increment it by 1
    left_sum = find_sum(fenwick_tree, left)
    right_sum = find_sum(fenwick_tree, right)

    return right_sum - left_sum


def update_fenwick_tree(fenwick_tree, index, original_value, updated_value):
    diff = updated_value - original_value

    while index < len(fenwick_tree):
        fenwick_tree[index] += diff
        index += find_lsb(index)


# FENWICK IS 1 INDEXED, 0th ELEMENT IS USELESS, fenwick_index = array_index+1
print(find_lsb(6))
fenwick_tree = make_fenwick_tree([3, 4, -2, 7, 3, 11, 5, -8, -9, 2, 4, -8])
print(fenwick_tree)
print(query_fenwick_tree(fenwick_tree, 3, 7))
# Pass here the index in the Fenwick Tree(NOT_IN_ARRAY), that is array_index+i
update_fenwick_tree(fenwick_tree, 7, 5, 8)
print(query_fenwick_tree(fenwick_tree, 3, 7))
