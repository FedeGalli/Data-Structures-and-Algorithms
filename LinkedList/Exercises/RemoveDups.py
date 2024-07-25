import Node

def removeDups(head : Node) -> Node:
    occourences = {}

    node = head
    prev = None
    while(node):

        if node.val not in occourences:
            occourences[node.val] = 1
            prev = node
        else:
            #remove node
            prev.next = node.next
        
        node = node.next
        

    return head


head = Node(5)
head.next = Node(4)
head.next.next = Node(5)
head.next.next.next = Node(4)
head.next.next.next.next = Node(3)
print(removeDups(head).visualizer())