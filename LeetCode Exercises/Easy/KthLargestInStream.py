#DO THIS WITH HEAPS


class KthLargest:
    def __init__(self, k, stream) -> None:
        self.k = k
        self.stream = stream
        self.maxes = self.calculateMaxs(k, stream)

    def calculateMaxs(self, k, stream) -> list:
        stream.sort()
        maxes = []

        for i in range(k):
            maxes.append(stream[-i - 1])

        return maxes
    
    def add(self, n):
        self.stream.append(n)
        for i, current_max in enumerate(self.maxes):
            if n > current_max:
                for j in range(self.k - 1, i, -1):
                    self.maxes[j] = self.maxes[j - 1]

                self.maxes[i] = n
                break
        return self.maxes[self.k - 1]



classe = KthLargest(3, [4, 5, 8, 2])

classe.add(3)
classe.add(5)
classe.add(10)
classe.add(9)
classe.add(4)