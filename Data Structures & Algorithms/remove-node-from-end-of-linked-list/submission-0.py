# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nth = head
        for i in range(n):
            if nth.next:
                nth = nth.next
            else:
                head = head.next
                return head
        slow = head
        while nth.next:
            slow = slow.next
            nth = nth.next
        slow.next = slow.next.next
        return head
        