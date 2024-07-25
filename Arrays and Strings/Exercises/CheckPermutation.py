#check if a string is a permutation of another

def checkPermutation(s1, s2):

    s2_mapping = {}

    if len(s1) != len(s2):
        return False

    for char in s2:
        if char not in s2_mapping:
            s2_mapping[char] = 1
        else:
            s2_mapping[char] += 1

    for char in s1:
        if char in s2_mapping:
            if s2_mapping[char] > 0:
                s2_mapping[char] -= 1
            else:
                return False
        else:
            return False
        
    return True

print(checkPermutation("ciao", "oiacc"))