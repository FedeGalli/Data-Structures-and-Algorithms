class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result_list = []
        visited = [False] * len(strs)
        
        for i in range(len(strs)):
            if (not visited[i]):
                visited[i] = True
                print(strs[i])
                anagram_pool = [strs[i]]
                for j in range(i + 1, len(strs)):
                    if self.isAnagram(strs[i], strs[j]):
                        anagram_pool.append(strs[j])
                        visited[j] = True
                
                result_list.append(anagram_pool)
        
        return result_list
    
    def isAnagram(self, s: str, t:str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {s_char : 0 for s_char in s}
        t_map = {t_char : 0 for t_char in t}

        for i in range(len(s)):
            s_map[s[i]] += 1
            t_map[t[i]] += 1

        for i in range(len(s)):
            if s_map.get(s[i]) != t_map.get(s[i]):
                return False

        return True
