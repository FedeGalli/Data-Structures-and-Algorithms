class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = self.stringCleaner(s)

        print(s)
        
        start = 0
        end = len(s) - 1

        while (start < end):
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1

        return True

    def stringCleaner(self, s: str) -> str:
        new_string = ""
        for char in s:
            if ord(char) < ord('a') or ord(char) > ord('z'):
                if ord(char) < ord('A') or ord(char) > ord('Z'):
                    if ord(char) < ord('0') or ord(char) > ord('9'):
                        continue
            
            new_string += char

        return new_string.lower()
