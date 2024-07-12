# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        reversed_stack = []
        current_node = 1
        node = head
        left_node = None
        while(current_node <= left):
            if left == current_node:
                left_node = node
                break

            current_node += 1
            node = node.next
        
        while(current_node <= right):
            reversed_stack.append(left_node.val)
            left_node = left_node.next
            current_node += 1

        for i in range(right - left + 1):
            node.val = reversed_stack.pop()
            node = node.next

        return head