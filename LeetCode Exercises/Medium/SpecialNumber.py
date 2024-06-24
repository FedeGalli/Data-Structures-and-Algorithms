class Solution:
    def minimumOperations(self, num: str) -> int:
        if int(num) % 25 == 0:
            return 0
        
        result = len(num)
        i = len(num) - 1
        while (result > len(num) - i):
            if num[i] == '0':
                counter = 0
                for j in range(i - 1, -1, -1):
                    if num[j] != '0' and num[j] != '5':
                        counter += 1
                    else:
                        break
                if (counter + len(num) - i - 1 < result):
                    result = counter + len(num) - i - 1
                

            if num[i] == '5':
                counter = 0
                for j in range(i - 1, -1, -1):
                    if num[j] != '2' and num[j] != '7':
                        counter += 1
                    else:
                        if (counter + len(num) - i - 1 < result):
                            result = counter + len(num) - i - 1

            
            i -= 1

        return result

            
            