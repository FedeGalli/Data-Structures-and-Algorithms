import math

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        justified_list = []
        string_formatter = [words[0]]
        counter = len(words[0])
        i = 1
        while(i <= len(words)):

            if i != len(words) and counter + len(words[i]) + 1 <= maxWidth:
                counter += len(words[i]) + 1
                string_formatter.append(words[i])
            
            else:
                n_of_words = len(string_formatter)
                n_of_spaces = maxWidth - counter + n_of_words - 1
                
                spaces_per_slot = n_of_spaces / (n_of_words - 1 if n_of_words >= 3 else 1)
                s = string_formatter[0]
                for word in string_formatter[1:]:
                    if s == "" and spaces_per_slot != math.ceil(spaces_per_slot):
                        s += (" " * math.ceil(spaces_per_slot)) + word 
                    else:
                        s += (" " * int(spaces_per_slot)) + word 
                                  
                justified_list.append(s)

                if i != len(words):
                    string_formatter = [words[i]]
                    counter = len(words[i])

            i += 1

        return justified_list