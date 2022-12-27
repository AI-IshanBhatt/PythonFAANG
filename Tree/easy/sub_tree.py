from typing import Optional
from .TreeNode import TreeNode

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Looks weird the recursive function has inner function
        def isSame(p, q):
            if not (p and q):
                return p is q
            else:
                return p.val == q.val and isSame(p.left, q.left) and isSame(p.right, q.right)

        if isSame(root, subRoot):
            return True
        if not root:
            return False
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)