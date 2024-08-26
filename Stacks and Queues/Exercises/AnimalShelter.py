class Shelter:
    class ListNode:
        def __init__(self, val, time, next=None):
            self.val = val
            self.next = next
            self.time = time

    def __init__(self):
        self.cat_shelter = None
        self.dog_shelter = None
        self.time = 0

    def enqueue(self, animal:str): #O(n)
        if animal == 'cat':
            if not self.cat_shelter:
                self.cat_shelter = ListNode(animal, self.time)
                self.time += 1
            else:
                node = self.cat_shelter
                while node:
                    node = node.next

                node = ListNode(animal)
        else:
            if not self.dog_shelter:
                self.dog_shelter = ListNode(animal, self.time)
                self.time += 1
            else:
                node = self.dog_shelter
                while node:
                    node = node.next

                node = ListNode(animal)


    def dequeueAny(self): #O(1)
        if not self.dog_shelter and not self.cat_shelter:
            return None
        if not self.dog_shelter:
            res = self.cat_shelter
            self.cat_shelter = self.cat_shelter.next if self.cat_shelter.next else None
            return res
        if not self.cat_shelter:
            res = self.dog_shelter
            self.dog_shelter = self.dog_shelter.next if self.dog_shelter.next else None
            return res

        if self.dog_shelter.time <= self.cat_shelter:
            res = self.dog_shelter
            self.dog_shelter = self.dog_shelter.next if self.dog_shelter.next else None
        else:
            res = self.cat_shelter
            self.cat_shelter = self.cat_shelter.next if self.cat_shelter.next else None

        return res

    def dequeueCat(self):
        if not self.cat_shelter:
            return None

        res = self.cat_shelter
        self.cat_shelter = self.cat_shelter.next if self.cat_shelter.next else None

        return res

    def dequeueDog(self):
        if not self.dog_shelter:
            return None

        res = self.dog_shelter
        self.dog_shelter = self.dog_shelter.next if self.dog_shelter.next else None

        return res
