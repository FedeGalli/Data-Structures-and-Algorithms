class Solution:
    def findComplement(self, num: int) -> int:
        res = ''

        for char in bin(num)[2:]:
            res += str((int(char) + 1) % 2)

        return int(res, 2)
