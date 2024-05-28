# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        elements = []
        self.traversal(root, elements)

        return elements
    
    def traversal(self, node, list):

        if node == None:
            return

        
        self.traversal(node.left, list)
        list.append(node.val)
        self.traversal(node.right, list)