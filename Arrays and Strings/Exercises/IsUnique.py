#A string contains all different charactes?

def isUnique(s : str) -> bool:

    if not s or s == "":
        return True
    
    string_map = {}
    for char in s:
        if char not in string_map:
            string_map[char] = 1
        else:
            return False
    
    return True


print(isUnique("abaabb"))