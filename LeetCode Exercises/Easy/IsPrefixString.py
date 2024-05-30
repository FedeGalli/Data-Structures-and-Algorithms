class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        
        
        total_length = 0
        for elem in words:

            if elem == s[total_length:len(elem) + total_length]:
                total_length += len(elem)
            else:
                return False

            if total_length == len(s):
                return True
        
        return False