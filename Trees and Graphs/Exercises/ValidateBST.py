class NodeTree:

    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.right = right
        self.left = left

def isBST(root):
    l = float("-inf")
    r = float("inf")

    def dfs(root, l, r):
        if not root:
            return True
        if root.val > l and root.val < r:
            return dfs(root.left, l, root.val) and dfs(root.right, root.val, r)
        else:
            return False


    return dfs(root, l, r)


root = NodeTree(8)
root.left = NodeTree(4)
root.right = NodeTree(10)
root.left.left = NodeTree(2)
root.left.right = NodeTree(6)

print(isBST(root))
