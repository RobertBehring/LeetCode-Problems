# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        size = 0
        while cur:
            cur = cur.next
            size += 1

        if size == n:
            return head.next

        i = size - n
        cur = head
        prev = cur
        while i:
            prev = cur
            cur = cur.next
            i -= 1
        prev.next = cur.next

        return head
