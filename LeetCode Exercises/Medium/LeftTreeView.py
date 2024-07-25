class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def leftView(root, left_view_nodes, current_level=1):

    if not root:
        return

    if current_level > len(left_view_nodes):
        left_view_nodes.append(root.val)

    print(root.val)

    
    leftView(root.left, left_view_nodes, current_level + 1)
    leftView(root.right, left_view_nodes, current_level + 1)


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(5)
tree.right.right.right = TreeNode(6)

left_view_nodes = []
leftView(tree, left_view_nodes, 1)
print(left_view_nodes)