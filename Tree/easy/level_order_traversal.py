from typing import Optional, List
from collections import deque
from TreeNode import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q, result = deque(), []
        q.append(root)

        while q:
            current = []  # Do not be afraid to declare multiple things in one line
            for i in range(len(q)):
                element = q.popleft()
                current.append(element.val)
                if element.left:
                    q.append(element.left)
                if element.right:
                    q.append(element.right)
            result.append(current)
        return result


    def levelOrderList(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        answer = []
        q = [root]  # See how smartly this is working as queue

        while q:
            answer.append([node.val for node in q])
            pairs = [(node.left, node.right) for node in q]
            q = [leaf for pair in pairs for leaf in pair if leaf]
        return answer

    def levelOrderFromMemory(self, root) -> List[List[int]]:

        q, result = [root], []

        while q:
            result.append([node.val for node in q])
            pairs = [(node.left, node.right) for node in q]
            q = [leaf for pair in pairs for leaf in pair if leaf]

        return result

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)

    # print(s.levelOrderList(root))
    print(s.levelOrderFromMemory(root))

