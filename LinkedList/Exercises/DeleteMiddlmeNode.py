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
def deleteMiddleNode(head : Node):

    node = head
    length = 0

    if not node.next.next:
        head = head.next

    while(node):
        length += 1
        node = node.next
    
    middle = length // 2

    node = head
    i = 0
    while(i < middle - 1):
        node = node.next
        i += 1

    node.next = node.next.next


head = Node(1)

head.next = Node(2)

head.next.next = Node(3)
head.next.next.next = Node(4)

deleteMiddleNode(head)

print(head.visualizer())