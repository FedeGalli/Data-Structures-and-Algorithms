#aabccccccaaa

def string_compressor(s):

    if not s:
        return s
    current_char = s[0]
    res = ''
    counter = 1
    for char in s[1:]:
        if char != current_char:
            res += current_char + str(counter)
            counter = 0
            current_char = char

        counter += 1

    res += current_char + str(counter)
    if len(res) >= len(s):
        return s

    return res


print(string_compressor("aabcaaa"))
