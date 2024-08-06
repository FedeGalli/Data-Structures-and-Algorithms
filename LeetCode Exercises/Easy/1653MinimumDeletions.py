def get_diameter(node):
    max = 0

    tree_recursion(node, max)

    return max

def tree_recursion(node, max):

    if not node:
        return 0
    
    max_l = get_diameter(node.left)
    max_r = get_diameter(node.right)
    max = max(max, max_l + max_r)

    return 1 + max(max_l, max_r)