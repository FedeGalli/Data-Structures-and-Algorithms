class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
           
            else:
                if stack == []:
                    return False
                if char ==  ")":
                    if stack.pop() != "(":
                        return False
                else:
                    if ord(char) - 2 != ord(stack.pop()):
                        return False
       
        if stack == []:
            return True
       
        return False
