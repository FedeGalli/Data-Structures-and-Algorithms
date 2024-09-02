class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = []

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
                res.append("")
            elif char == ")":
                if len(stack) > 0:
                    res.append(")")
                    res[stack.pop()] = "("
                else:
                    res.append("")
            else:
                res.append(char)

        return "".join(res)
