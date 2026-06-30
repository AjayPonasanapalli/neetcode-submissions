# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        l = dummy
        for _ in range(left-1):
            l = l.next
        tail = l 
        l=l.next
        r = l 
        for _ in range(right - left):
            r = r.next
        print(r.val,l.val)
        curr,prev = l,None
        stop = r.next
        while curr != stop:
            next_node = curr.next
            curr.next = prev
            prev = curr 
            curr = next_node
        tail.next = prev
        l.next = stop
        
        


        return dummy.next