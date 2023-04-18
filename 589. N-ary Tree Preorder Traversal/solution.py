"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        preorder_list = list()

        self.depth_first_search(root, preorder_list)

        return preorder_list

    def depth_first_search(self, root, preorder_list):
        if root is None:
            return

        preorder_list.append(root.val)

        for child in root.children:
            self.depth_first_search(child, preorder_list)