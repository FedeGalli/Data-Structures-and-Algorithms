class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        stack.append(len(temperatures) - 1)

        for i in range(len(temperatures) - 2, -1, -1):
            while(len(stack) > 0 and temperatures[i] >= temperatures[stack[-1]]):
                stack.pop()
            
            if len(stack) > 0:
                res[i] = (stack[-1] - i)
            
            stack.append(i)

        return res