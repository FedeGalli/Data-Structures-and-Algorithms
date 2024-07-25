class Node:
    def __init__(self, val=None, next=None):
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

class MinStack:


    def __init__(self):
        self.stack_head = None
        self.min_stack_head = None

    def pop(self):
        if not self.stack_head:
            return None
        
        poped_item = self.stack_head.val
        self.stack_head = self.stack_head.next
        
        self.min_stack_head = self.min_stack_head.next

        return poped_item


    def push(self, item):
        if not self.stack_head:
            self.stack_head = Node(item)
            self.min_stack_head = Node(item)

        else:
            self.stack_head = Node(item, self.stack_head)

            if item < self.min_stack_head.val:
                self.min_stack_head = Node(item, self.min_stack_head)
            else:
                self.min_stack_head = Node(self.min_stack_head.val, self.min_stack_head)


    def min(self):
        return self.min_stack_head.val
    

stack = MinStack()

stack.push(10)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(-1)

print(stack.min())

stack.pop()

print(stack.min())