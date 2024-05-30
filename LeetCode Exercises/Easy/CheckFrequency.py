class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        dic = {}

        for char in s:

            if dic.get(char, None) == None:
                dic[char] = 0

            dic[char] += 1

        
        ref_val = dic[s[0]]
        for occourences in dic.values():
            if occourences != ref_val:
                return False
        
        return True

