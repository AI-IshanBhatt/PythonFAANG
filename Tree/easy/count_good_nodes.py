from math import inf

from Tree.easy.TreeNode import TreeNode


def goodNodes(root: TreeNode) -> int:

    count = 0

    def dfs(root, max_here):
        if root.val >= max_here:
            count += 1
            max_here = root.val

        if root.left:
            dfs(root.left, max_here)
        if root.right:
            dfs(root.right, max_here)

    dfs(root, float(-inf))
    return count


class Solution:
    pass

