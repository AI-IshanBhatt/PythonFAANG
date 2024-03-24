"""
/*
*        10
*   16          5
* 1   -3      6    11
*           4
* */

"""
from TreeNode import TreeNode
from collections import deque


def max_at_each_level(root):
    queue = deque([root])
    max_at_levels = []

    while queue:
        max_at_levels.append(max(n.val for n in queue))
        for _ in range(len(queue)):
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    return max_at_levels


def max_at_each_level_cool(root):
    queue = deque([root])
    max_at_levels = []

#     DO NOT MUTATE THE QUEUE BUT RE-ASSIGN IT
    while queue:
        max_at_levels.append(max(n.val for n in queue))
        pairs = [(node.left, node.right) for node in queue]
        queue = [node for pair in pairs for node in pair if node]

    return max_at_levels


def sum_at_each_level(root):
    queue, sum_levels = deque([root]), []

    while queue:
        sum_levels.append(sum(n.val for n in queue))
        pairs = [(node.left, node.right) for node in queue]
        queue = [node for pair in pairs for node in pair if node]

    return sum_levels


def avg_at_each_level(root):
    queue, avg_levels = deque([root]), []  # No need for queue to be deque here, see side_view(root, side)

    while queue:
        avg_levels.append(sum(n.val for n in queue) / len(queue))
        pairs = [(node.left, node.right) for node in queue]
        queue = [node for pair in pairs for node in pair if node]

    return avg_levels


def avg_at_each_level_uncool(root):
    queue, avg_levels, current_sum = deque([root]), [], 0

    while queue:
        current_len, current_sum = len(queue), 0
        for _ in range(current_len):
            current_node = queue.popleft()
            current_sum += current_node.val

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        avg_levels.append(current_sum / current_len)

    return avg_levels


def side_view(root, side):
    queue, left_side = [root], []

    side = 0 if side == "left" else -1

    while queue:
        left_side.append(queue[side].val)
        pairs = [(node.left, node.right) for node in queue]
        queue = [node for pair in pairs for node in pair if node]

    return left_side


if __name__ == "__main__":
    treenode = TreeNode(10)
    treenode.left = TreeNode(16)
    treenode.right = TreeNode(5)

    treenode.left.left = TreeNode(1)
    treenode.left.right = TreeNode(-3)

    treenode.right.left = TreeNode(6)
    treenode.right.right = TreeNode(11)
    treenode.right.left.left = TreeNode(4)

    print(max_at_each_level(treenode))
    print(max_at_each_level_cool(treenode))

    print(sum_at_each_level(treenode))
    print(avg_at_each_level(treenode))
    print(avg_at_each_level_uncool(treenode))

    print(side_view(treenode, side="left"))
    print(side_view(treenode, side="right"))