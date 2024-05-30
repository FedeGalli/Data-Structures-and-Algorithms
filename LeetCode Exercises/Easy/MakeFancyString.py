class Solution:
    def makeFancyString(self, s: str) -> str:
        counter = 1
        result = s[0]

        if len(s) < 3:
            return s
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                counter += 1
            else:
                counter = 1
            
            if counter != 3:
                result += s[i]
            else:
                counter -= 1
        
        return result