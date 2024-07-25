class Node:

    def __init__(self, val=0):
        self.val = val
        self.next = None


class TreeNode:

    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def problem(head):

    levels = []

    populate_levels(head, 0, levels)

    return levels

def populate_levels(head, current_level, levels):

    if not head:
        return
    
    if len(levels) == current_level:
        levels.append(Node(head.val))
    else:
        node = levels[current_level]
        while(node.next):
            node = node.next
        node.next = Node(head.val)

    populate_levels(head.left, current_level + 1, levels)
    populate_levels(head.right, current_level + 1, levels)



tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)


print(problem(tree)[2].next.next.val)