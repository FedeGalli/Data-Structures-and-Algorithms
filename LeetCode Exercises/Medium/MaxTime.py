def maxTime(s):

    s = list(s)
    
    if s[0] == "?":
        s[0] = "2" if (s[0] == "?" or int(s[1]) <= 3) else "1"
    
    if s[1] == "?":
        s[1] = "3" if int(s[0]) == 2 else "9"

    if s[3] == "?":
        s[3] = 5
    
    if s[4] == "?":
        s[4] = "9" 

    return s
print(maxTime("0?:??"))