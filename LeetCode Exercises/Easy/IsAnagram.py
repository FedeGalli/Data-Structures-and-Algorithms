class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        dict_s = {s_char : 0 for s_char in s}
        dict_t = {t_char : 0 for t_char in t}

        for i in range(len(s)):
            dict_s[s[i]] += 1
            dict_t[t[i]] += 1

        for s_char in s:

            if dict_s.get(s_char) != dict_t.get(s_char):
                return False
        
        return True
