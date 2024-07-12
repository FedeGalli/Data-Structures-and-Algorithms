class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}
        for i in range(len(s)):
            if s[i] not in s_map.keys():
                s_map[s[i]] = 1
            else:
                s_map[s[i]] += 1
            
            if t[i] not in t_map.keys():
                t_map[t[i]] = 1
            else:
                t_map[t[i]] += 1

        for s_key in s_map.keys():
            if s_key not in t_map.keys() or t_map[s_key] != s_map[s_key]:
                return False
        return True
