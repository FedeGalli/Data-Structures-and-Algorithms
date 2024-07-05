class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack:
    
    def __init__(self, data) -> None:
        self.top = Node(data)

    
    def add(self, data):

        x = self.top
        self.top = Node(data)
        self.top.next = x

    def pop(self) -> object:

        return_val = self.top
        self.top = self.top.next

        return return_val
    
    def visualize(self) -> str:
        
        x = self.top
        return_str = x.data
        while(x.next != None):

            x = x.next
            return_str += "\n" + x.data
        
        return return_str
    

x = Stack("1")
x.add("2")
x.add("3")

print(x.visualize())

x.pop()

print(x.visualize())