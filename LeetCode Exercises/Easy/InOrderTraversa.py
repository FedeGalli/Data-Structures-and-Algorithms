# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        print_list = []

        self.recursive(root, print_list)
        return print_list
    

    def recursive(self, root, print_list):

        if root == None:
            return

        self.recursive(root.left, print_list)
        print_list.append(root.val)
        self.recursive(root.right, print_list)