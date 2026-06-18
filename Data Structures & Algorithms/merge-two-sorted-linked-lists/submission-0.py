# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first,second = list1,list2
        head,last=None,None
        if not first:
            head = second 
            return head
        if not second:
            head= first
            return head

        while first and second:
            if last is None:
                if first.val<=second.val:
                    last=first
                    head = first
                    first = first.next
                    
                else:
                    last = second
                    head = second
                    second = second.next 
                    
            else:
                if first.val<=second.val:
                    last.next=first
                    first = first.next
                else:
                    last.next = second
                    second = second.next 
                last = last.next
        if first:
            last.next = first
        else:
            last.next = second

        return head
        