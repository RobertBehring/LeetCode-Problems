# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # return self.recHasPathSum(root, targetSum)
        return self.iterHasPathSum(root, targetSum)


    def iterHasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        de = [(root, targetSum-root.val)]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                de.append((node.right, curr_sum-node.right.val))
            if node.left:
                de.append((node.left, curr_sum-node.left.val))
        return False


    def recHasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
