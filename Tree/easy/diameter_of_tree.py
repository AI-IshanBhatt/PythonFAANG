from typing import Optional
from .TreeNode import TreeNode

# Let's call this pattern calculating something and setting something else
# Very important in tree and se how it works with Python
class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # This is very important, in LC questions you will have to create these kinds of variable with self
        self.diameter = 0

        def get_diameter(root):
            if root is None: return 0

            left = get_diameter(root.left)
            right = get_diameter(root.right)

            # I am the answer
            self.diameter = max(self.diameter, left + right)

            # Diameter passes through me
            return 1 + max(left, right)

        get_diameter(root)
        return self.diameter