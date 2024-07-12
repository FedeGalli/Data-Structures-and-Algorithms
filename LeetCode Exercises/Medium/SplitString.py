def split(s):
    poss = 0
    
    for i in range(len(s)):
        if unique(s[:i], s[i:]):
            poss += 1
    
    return poss

def unique(s1, s2):
    map1 = {}
    map2 = {}

    for char in s1:
        map1[char] = 1

    for char in s2:
        map2[char] = 1
    
    return sum(map1.values()) == sum(map2.values())


print(split("aaaa"))