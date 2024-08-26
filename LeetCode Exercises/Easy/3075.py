class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort() #O(nlogn)
        res = 0
        i = 0
        while i < k:
            curr_max = happiness.pop()
            if i > curr_max:
                return res
            res += curr_max - i
            i += 1

        return res
