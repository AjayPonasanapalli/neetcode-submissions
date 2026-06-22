# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        head2 = l2 
        int1 = ''
        int2 = ''
        while head1:
            int1 += str(head1.val)
            head1 = head1.next
            
        while head2:
            int2 += str(head2.val)
            head2 = head2.next
        ans = int(int1[::-1])+int(int2[::-1])
        if ans == 0:
            return ListNode()
        temp = ListNode()
        head = temp
        while ans:
            rem = ans%10
            ans = ans//10
            curr = ListNode(rem)
            temp.next = curr 
            temp = curr
        return head.next