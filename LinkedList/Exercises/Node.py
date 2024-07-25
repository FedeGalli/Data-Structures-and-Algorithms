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