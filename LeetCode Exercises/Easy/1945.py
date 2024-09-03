class Solution:
    def getLucky(self, s: str, k: int) -> int:

        starting_num = ""

        for char in s:
            starting_num += str(ord(char) % (ord('a') - 1))


        for i in range(k):
            res = 0
            for char in starting_num:
                res += int(char)

            starting_num = str(res)


        return int(starting_num)
