# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res_list = []

        self.bfs(root, 0, res_list)

        return res_list
    
    def bfs(self, root, depth, res_list):
        if not root:
            return


        if depth == len(res_list):
            res_list.append([])
            
        res_list[depth].append(root.val)

        self.bfs(root.left, depth + 1, res_list)
        self.bfs(root.right, depth + 1, res_list)