# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        result = head
        prev = head
        next = head.next

        if next == None:
            return head

        while(next != None):
            if next.val == prev.val:
                prev.next = next.next
                next = prev.next
            else:
                prev = next
                next = next.next

        return result