"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""

class Solution:
    def isValid(self, s: str) -> bool:
        order = []
        if len(s) % 2 == 1 or len(s) == 0:
            return False

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                order.append(s[i])
            else:
                if (s[i] == ')' and order.top() == '('):
                    order.pop()
                elif (s[i] == ']' and order.top() == '['):
                    order.pop()
                elif (s[i] == '}' and order.top() == '{'):
                    order.pop()
                else:
                    return False
        
        return True
                    
