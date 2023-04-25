from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def potInvert(node):
            """DFS POT of binary tree"""
            if not node:
                return

            potInvert(node.left)
            potInvert(node.right)

            node.left, node.right = node.right, node.left

        # potInvert(root)
        self.iterInvertTree(root)
        return root

    def iterInvertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        q = deque()
        q.append(root)

        while q:
            cur = q.popleft()
            cur.left, cur.right = cur.right, cur.left

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        return root
