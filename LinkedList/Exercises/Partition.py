class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def visualizer(self):
        node = self
        s = ""
        while(node):
            if node.next == None:
                s += str(node.val)
            else:
                s += str(node.val) + " -> "

            node = node.next
        
        return s
    


def partition(head : Node, k : int) -> Node:

    node = head
    new_head = Node(node.val)
    new_node = new_head
    node = node.next
    while(node):
        if node.val >= k:
            new_node.next = Node(node.val)
            new_node = new_node.next
        else:
            new_head = Node(node.val, new_head)

        node = node.next

    
    return new_head


head = Node(1)
head.next = Node(4)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)
head.next.next.next.next = Node(1)


print(partition(head, 3).visualizer())