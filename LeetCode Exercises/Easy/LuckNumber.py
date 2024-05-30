class Solution:

    def converter(self, s: str) -> str:

        converted_number = ""
        for char in s:
            converted_number += str(ord(char) - ord('a') + 1)

        return converted_number

    def getLucky(self, s: str, k: int) -> int:
        

        str_number = self.converter(s)

        number_list = [*str_number]
        for i in range(k):
            sum = 0
            for elem in number_list:
                sum += int(elem)

            
            number_list = [*str(sum)]
        
        return sum
