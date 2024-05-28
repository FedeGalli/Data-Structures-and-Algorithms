# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        current_node = head

        if current_node.next == None:
            return None

        nodes = []


        while (current_node != None):

            nodes.append(current_node)
            current_node = current_node.next

        
        if len(nodes) == n:
            head = nodes[1]
        elif n == 1:
            prevNode = nodes[len(nodes) - n - 1]
            prevNode.next = None
        else:
            prevNode = nodes[len(nodes) - n - 1]
            prevNode.next = prevNode.next.next


        return head
