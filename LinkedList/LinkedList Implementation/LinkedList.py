class LinkedList:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    
    def add(self, data) -> None:
        linked_list = self

        while (linked_list.next != None):
            linked_list = linked_list.next
        
        linked_list.next = LinkedList(data)

    def remove_at(self, index):
        i = 0
        linked_list = self

        if index < 0:
            return None
        if index == 0:
            earsed_item = linked_list
            linked_list = linked_list.next
            return earsed_item
            
        while (i < index - 1):
            if linked_list == None:
                return None
            
            linked_list = linked_list.next
            if linked_list.next == None:
                return None
            i += 1
        
        earsed_item = linked_list.next
        linked_list.next = linked_list.next.next
        return earsed_item
    
    def get(self, index):
        i = 0
        linked_list = self

        while (i < index):
            linked_list = linked_list.next
            i += 1
        
        return linked_list.next

    def visualize(self) -> str:
        linked_list = self
        final_string = linked_list.data

        while (linked_list.next != None):
            linked_list = linked_list.next
            final_string += " -> " + linked_list.data
        
        return final_string

    def tmp(self):
        ll = self

        ll = ll.next


ll = LinkedList("1")

ll.add("2")

ll.add("3")

print(ll.visualize())

ll.tmp()

#print(ll.remove_at(0).data)
print(ll.visualize())

ll.add("4")

print(ll.visualize())