    # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverseList(self, head):
        if not head:
            return None
            
        new_linked_list = None
        current_node = head
        while(current_node):
            tmp = new_linked_list
            new_linked_list = ListNode(current_node.val)
            new_linked_list.next = tmp

        return new_linked_list
    

