import math
class Solution:
    def reverse(self, x: int) -> int:
        maxInt = (2 ** 31) - 1
        coeficent = 1
        if x < 0:
            coeficent = -1
            x = abs(x)

        sRes = ""
        while x >= 1:
            sRes = sRes + str(x % 10)
            x = math.floor(x / 10)


        res = 0
        for i, char in enumerate(sRes):
            res += int(char) * (10**(len(sRes) - i - 1))

            if res >= maxInt:
                return 0

        return res * coeficent
