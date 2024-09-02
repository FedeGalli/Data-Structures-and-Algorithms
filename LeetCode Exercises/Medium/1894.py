class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        chalk_sum = 0
        for num in chalk: #o(n)
            chalk_sum += num

        k = k % chalk_sum

        for i in range(len(chalk)): #o(n)
            k -= chalk[i]

            if k < 0:
                return i
