def string_rotation(self, s1, s2):
    reversed_string = ""
    stack = []
    for char in s1:
        stack.append(char)


    while len(stack) > 0:
        reversed_string += stack.pop()
