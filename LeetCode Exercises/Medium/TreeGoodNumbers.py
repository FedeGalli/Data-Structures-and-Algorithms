# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        return self.maxInPath(root, -101)
        
    def maxInPath(self, root, max_num):
        
        if not root:
            return 0
        
        res = 0
        
        if root.val >= max_num:
            max_num = root.val
            res = 1

        res += self.maxInPath(root.left, max_num)
        res += self.maxInPath(root.right, max_num)

        return res