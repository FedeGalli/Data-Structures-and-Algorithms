class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        current = []
        current_set = set()
        def backtracking(i):
            if i >= len(nums):
                current_copy = ''.join(str(x) for x in current.copy())
                if current_copy not in current_set:
                    current_set.add(current_copy)
                    res.append(current.copy())
                return

            current.append(nums[i])
            backtracking(i + 1)

            current.pop()
            backtracking(i + 1)

        backtracking(0)

        return res
