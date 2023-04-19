# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        nodes = list()
        while cur:
            if cur in nodes:
                return nodes[nodes.index(cur)]
            nodes.append(cur)
            cur = cur.next
