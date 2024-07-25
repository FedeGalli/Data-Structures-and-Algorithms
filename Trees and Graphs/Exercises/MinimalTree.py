# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#             ^


class TreeNode:

    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def generate_binary_search_tree(sorted_list, head):

    head = TreeNode(sorted_list[len(sorted_list) // 2])
    node = head
    generate_with_recursion(node, sorted_list)


def generate_with_recursion(head, list):

    if not len(list):
        return

    left_slice = list[:len(list)  // 2]
    right_slice = list[len(list) + 1 // 2:]

    head.left = left_slice[len(left_slice) // 2]
    head.right = right_slice[len(right_slice) // 2]

    generate_with_recursion(head.left, left_slice)
    generate_with_recursion(head.right, right_slice)



