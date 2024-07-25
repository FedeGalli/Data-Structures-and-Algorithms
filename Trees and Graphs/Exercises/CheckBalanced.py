class TreeNode:

    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def check_balanced(head, x):

    if not head:
        return 0


    l = check_balanced(head.left, x) + 1
    r = check_balanced(head.right, x) + 1

    print(str(head.val) + " " + str(l) + " " + str(r))
    if abs(l - r) > 1:
        x.append(1)

    return max(l, r)

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

x = []
check_balanced(tree, x)

print(len(x) == 0)