# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
       
        right_nodes = []




        self.dfs(root, right_nodes, 1)
        return right_nodes


    def dfs(self, root: TreeNode, right_nodes: List[int], current_depth):
       
        if not root:
            return
       
        if current_depth > len(right_nodes):
            right_nodes.append(root.val)


        self.dfs(root.right, right_nodes, current_depth + 1)
        self.dfs(root.left, right_nodes, current_depth + 1)