# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        def helper(node, level):
            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels

# def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#     traversal = []

#     self.levelOrderTraversal(root, 0, traversal)

#     return traversal

# def levelOrderTraversal(self, root, level, traversal):
#     if root is None:
#         return

#     try:
#         traversal[level].append(root.val)
#     except:
#         traversal.append([root.val])

#     self.levelOrderTraversal(root.left, level+1, traversal)
#     self.levelOrderTraversal(root.right, level+1, traversal)
