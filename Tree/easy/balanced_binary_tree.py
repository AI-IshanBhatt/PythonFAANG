# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True

        def get_height(root):
            if root is None: return 0

            l, r = get_height(root.left), get_height(root.right)

            if abs(l - r) > 1:
                self.is_balanced = False

            return 1 + max(l, r)

        get_height(root)
        return self.is_balanced