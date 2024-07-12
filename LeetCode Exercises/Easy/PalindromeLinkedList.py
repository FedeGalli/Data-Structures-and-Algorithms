# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        
        if node.val == None:
            return False
        stack = []

        while(node != None):
            stack.append(node.val)
            node = node.next
        
        node = head
        while(node != None):
            if node.val != stack.pop():
                return False
            node = node.next
        return True