# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        counter = 1
        to_edit_list = list1
        return_list = to_edit_list
        while(to_edit_list != None):
            if a == counter:
                #merge
                end_list = to_edit_list.next
                while (b - counter >= 0):
                    end_list = end_list.next
                    counter += 1
                
                to_edit_list.next = list2
                while(to_edit_list != None):
                    to_edit_list = to_edit_list.next
                
                to_edit_list.next = end_list

                return return_list
            else:
                to_edit_list = to_edit_list.next
                counter += 1