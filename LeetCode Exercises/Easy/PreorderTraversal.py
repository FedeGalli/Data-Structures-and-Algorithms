# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        dataList = []

        self.preorderTraversal1(root, dataList)

        return dataList
    
    def preorderTraversal1(self, node, dataList):

        if node == None:
            return
        
        dataList.append(node.val)
        self.preorderTraversal1(node.left, dataList)
        self.preorderTraversal1(node.right, dataList)
