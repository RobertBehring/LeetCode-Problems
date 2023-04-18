# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        num_nodes = 0
        while cur:
            cur = cur.next
            num_nodes += 1

        mid = num_nodes // 2
        cur = head
        while mid > 0:
            cur = cur.next
            mid -= 1

        return cur