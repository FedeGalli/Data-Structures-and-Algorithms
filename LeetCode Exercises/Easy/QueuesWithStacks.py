class MyQueue:

    def __init__(self):
        self.main_stack = []

    def push(self, x: int) -> None:
        self.main_stack.append(x)

    def pop(self) -> int:
        if len(self.main_stack) == 0:
            return

        tmp_stack = []
        pop_val = None

        for i in range(len(self.main_stack) - 1):
            pop_val = self.main_stack.pop()
            tmp_stack.append(pop_val)

        pop_val = self.main_stack.pop()

        for i in range(len(tmp_stack)):
            val = tmp_stack.pop()
            self.main_stack.append(val)
        
        return pop_val

    def peek(self) -> int:
        if len(self.main_stack) == 0:
            return

        tmp_stack = []
        pop_val = None

        for i in range(len(self.main_stack)):
            pop_val = self.main_stack.pop()
            tmp_stack.append(pop_val)

        for i in range(len(tmp_stack)):
            val = tmp_stack.pop()
            self.main_stack.append(val)
        
        return pop_val

    def empty(self) -> bool:
        return len(self.main_stack) == 0