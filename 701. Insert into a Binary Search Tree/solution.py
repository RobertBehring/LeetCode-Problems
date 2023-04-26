# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[
        TreeNode]:
        if not root:
            return TreeNode(val)
        cur = root
        while cur:
            prev = cur
            left, right = cur.left, cur.right
            isLeft = True if val < cur.val else False
            cur = left if isLeft else right
            if not cur:
                if isLeft:
                    prev.left = TreeNode(val)
                else:
                    prev.right = TreeNode(val)
                break
        return root
