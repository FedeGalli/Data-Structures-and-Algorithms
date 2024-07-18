# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2

        if p1 == None and p2 == None:
            return None
        if p1 == None:
            return p2
        if p2 == None:
            return p1

        merged_list = None
        head = None

        if p1.val < p2.val:
            merged_list = ListNode(p1.val)
            p1 = p1.next
        else:
            merged_list = ListNode(p2.val)
            p2 = p2.next

        head = merged_list
        while(p1 or p2):
            if p1 == None:
                merged_list.next = ListNode(p2.val)
                p2 = p2.next
            elif p2 == None:
                merged_list.next = ListNode(p1.val)
                p1 = p1.next
            else:
                if p1.val >= p2.val:
                    merged_list.next = ListNode(p2.val)
                    p2 = p2.next
                else:
                    merged_list.next = ListNode(p1.val)
                    p1 = p1.next

            merged_list = merged_list.next

        return head