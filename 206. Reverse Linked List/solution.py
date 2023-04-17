# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if head is None:
            return

        prev = head
        cur = head.next
        prev.next = None
        while cur:
            temp = cur
            cur = cur.next
            temp.next = prev
            prev = temp
        return prev
