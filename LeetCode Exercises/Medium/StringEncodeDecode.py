class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_word = ""

        for word in strs:
            encoded_word += word + "\\0"
        
        print(encoded_word)
        return encoded_word
    def decode(self, s: str) -> List[str]:
        return_list = []
        word = ""

        i = 0
        while(i < len(s)):
            if s[i] == "\\" and s[i + 1] == '0':
                return_list.append(word)
                word = ""
                i += 1
            else:
                word += s[i]
            
            i += 1

        return return_list