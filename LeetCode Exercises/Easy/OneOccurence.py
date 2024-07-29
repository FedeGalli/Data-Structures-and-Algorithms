def solution(s : str) -> str:

    char_map = {}

    for char in s:        
        char_map[char] = 1 + char_map.get(char, 0)

    for entry in char_map:
        if char_map[entry] == 1:
            return entry
        
    
    return "_"



s = "abaabad"

print(solution(s))