"""
/* USE THIS TO GET ALL PATHS FROM ROOT TO ALL LEAF NODES AS WELL
*        10
*   16          5
* 1   -3      6    11
*           10
* */
TODO - Know the difference between global and nonlocal
"""
import sys

from TreeNode import TreeNode


def sum_path_to_root_exists_with_helper(root, total):
    path_exists = False

    def helper(root, total):
        if total == 0:
            nonlocal path_exists
            path_exists = True
            return
        if not root:
            return
        else:
            helper(root.left, total - root.val)
            helper(root.right, total - root.val)

    helper(root, total)
    return path_exists


def sum_path_to_root_exists_without_helper(root, total):

    if total == 0:
        return True

    if not root:
        return False

    return sum_path_to_root_exists_without_helper(root.left, total - root.val) or\
        sum_path_to_root_exists_without_helper(root.right, total - root.val)


def all_paths_from_root(root):
    all_paths = []

    def helper(root, temp_path):
        if not root:
            return

        if not(root.left or root.right):
            # Keep in mind if you use this trick to check leaf node, you still need to process the value of current node
            all_paths.append(temp_path + [root.val])

        helper(root.left, temp_path + [root.val])
        helper(root.right, temp_path + [root.val])

    helper(root, [])
    return all_paths


def all_paths_from_root_with_given_sum(root, total):
    all_paths = []

    def helper(root, total, temp_path):
        if not root:
            return
        if root.val == total:
            all_paths.append(temp_path + [root.val])
            return

        helper(root.left, total - root.val, temp_path + [root.val])  # THIS IS VERY POWERFUL TOOL - Kills Java each time
        helper(root.right, total - root.val, temp_path + [root.val]) # THIS IS VERY POWERFUL TOOL - Kills Java each time

    helper(root, total, [])
    return all_paths


def max_sum_dfs(root):

    def helper(root, running_sum):
        if not root:
            return 0
        if not(root.left or root.right):
            # Keep in mind if you use this trick to check leaf node, you still need to process the value of current node
            return running_sum + root.val
        return max(helper(root.left, running_sum + root.val), helper(root.right, running_sum + root.val))

    return helper(root, 0)


def path_with_maximum_sum(root):
    answer = []
    max_sum = -sys.maxsize

    def helper(root, running_sum, temp_path):
        nonlocal max_sum, answer
        if not root:
            return
        if not(root.left or root.right):
            if running_sum + root.val > max_sum:
                max_sum = running_sum + root.val
                answer = temp_path + [root.val]

        helper(root.left, running_sum+root.val, temp_path+[root.val])
        helper(root.right, running_sum + root.val, temp_path + [root.val])

    helper(root, 0, [])
    return answer


def simple_dfs(root):

    if root:
        print(root.val, end=" ")
        simple_dfs(root.left)
        simple_dfs(root.right)


if __name__ == "__main__":
    treenode = TreeNode(10)
    treenode.left = TreeNode(16)
    treenode.right = TreeNode(5)

    treenode.left.left = TreeNode(1)
    treenode.left.right = TreeNode(-3)

    treenode.right.left = TreeNode(6)
    treenode.right.right = TreeNode(11)
    treenode.right.left.left = TreeNode(10)

    # print(sum_path_to_root_exists_with_helper(treenode, 25))
    # print(sum_path_to_root_exists_without_helper(treenode, 25))

    # print(all_paths_from_root_with_given_sum(treenode, 26))
    # print(all_paths_from_root(treenode))

    print(max_sum_dfs(treenode))
    print(path_with_maximum_sum(treenode))

    simple_dfs(treenode)