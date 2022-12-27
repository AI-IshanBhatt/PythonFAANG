from math import inf
from typing import Optional
from .TreeNode import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst_checker(root, min_val, max_val):
            if not root:
                return True
            return min_val < root.val < max_val and bst_checker(root.left, min_val, root.val) and bst_checker(
                root.right, root.val, max_val)

        return bst_checker(root, float(-inf), float(inf))