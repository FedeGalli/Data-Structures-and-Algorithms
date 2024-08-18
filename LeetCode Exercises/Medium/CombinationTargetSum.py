class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def DFS(i, cur, total):
            if total > target or i >= len(nums):
                return
            if total == target:
                res.append(cur.copy())
                return

            cur.append(nums[i])
            DFS(i, cur, nums[i] + total)

            cur.pop()
            DFS(i + 1, cur, total)

        DFS(0, [], 0)

        return res
