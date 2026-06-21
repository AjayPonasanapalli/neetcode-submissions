"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        h = head
        new_head = None
        while h:
            if h == head:
                new_head = Node(h.val,h.next,h.random)
                prev = new_head
            else:
                curr = Node(h.val,h.next,h.random)
                prev.next = curr 
                prev = curr
            
            h=h.next
        new_map = {}
        h = head
        new_h = new_head
        while h:
            new_map[h] = new_h 
            h = h.next
            new_h = new_h.next
        h = head
        new_h = new_head
        while h:
            if h.random:
                new_h.random = new_map[h.random]
            else:
                new_h.random = None
            h = h.next
            new_h = new_h.next
        return new_head
            
        