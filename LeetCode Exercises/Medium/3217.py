# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        numsMap = set()
        for num in nums:
            numsMap.add(num)

        res = None
        prev = None

        while head:
            #skipping initial values
            print(head.val)
            if not res:
                if head.val not in numsMap:
                    prev = head
                    res = prev

            else:
                if head.val in numsMap:
                    if head.next:
                        prev.next = head.next
                    else:
                        prev.next = None
                else:
                    prev = prev.next

            head = head.next

        return res
