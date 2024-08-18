class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kth = []
        self.DFS(root, kth)
        return kth[k - 1]
    def DFS(self, root, kth):
        if not root or len(kth) == k:
            return

        self.DFS(root.left, kth)
        kth.append(root.val)
        self.DFS(root.right, kth)
