# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        p1 = head
        p2 = head.next

        while(p1 and p2):
            if p1 == p2:
                return True

            p1 = p1.next if p1 else None
            p2 = p2.next.next if p2 and p2.next else None

        return False