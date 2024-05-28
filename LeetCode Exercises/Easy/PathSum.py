# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        sum = 0

        return self.traversal(root, targetSum, sum)


    def traversal(self, node, targetSum, sum):

        if node == None:
            return False

        if node.left == None and node.right == None:
            if sum + node.val == targetSum:
                return True
            else:
                return False

        sum += node.val
        return self.traversal(node.left, targetSum, sum) or self.traversal(node.right, targetSum, sum)