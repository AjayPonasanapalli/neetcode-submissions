# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        h1  = head 
        slow,fast = head,head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
           
        
        curr,prev = slow.next,None
        slow.next = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr =next_node

        h2 = prev
        temp = ListNode()
        new_head = temp
        while temp and h1 and h2:
            temp.next = h1
            h1 = h1.next
            temp.next.next = h2
            h2 = h2.next
            temp = temp.next.next
        if h1:
            temp.next = h1 
        elif h2:
            temp.next = h2         