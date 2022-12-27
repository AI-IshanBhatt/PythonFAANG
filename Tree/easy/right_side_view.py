from typing import Optional, List
from collections import deque
from .TreeNode import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q, answer = deque(), []
        q.append(root)

        while q:
            answer.append(q[0].val)
            for i in range(len(q)):
                element = q.popleft()
                if element.right:
                    q.append(element.right)
                if element.left:
                    q.append(element.left)
        return answer

    def rightSideViewListComprehension(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = [root]
        answer = []

        while q:
            answer.append(q[0].val)
            pairs = [(node.right, node.left) for node in q]
            q = [leaf for pair in pairs for leaf in pair if leaf]

        return answer

