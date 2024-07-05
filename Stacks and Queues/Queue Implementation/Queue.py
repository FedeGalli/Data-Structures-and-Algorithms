class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Queue:

    def __init__(self, data) -> None:
        self.head = Node(data)
    
    def enqueue(self, data) -> None:
        if self.head == None:
            self.head = Node(data)
            return
        
        temp = self.head

        while (temp.next != None):
            temp = temp.next

        temp.next = Node(data)

    def dequeue(self) -> Node:
        if self.head == None:
            return
        
        return_val = self.head
        self.head = self.head.next

        return return_val
    
    def visualizer(self) -> str:
        tmp = self.head

        str_val = tmp.data

        while(tmp.next != None):
            tmp = tmp.next
            str_val = tmp.data + " -> " + str_val

        return str_val
    

q = Queue("0")

q.enqueue("1")
q.enqueue("2")
q.enqueue("3")

print(q.visualizer())

q.dequeue()

print(q.visualizer())
