class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        substring = []


        def DFS(i):
            if i >= len(nums):
                res.append(substring.copy())
                return

            #choosing to pick the number
            substring.append(nums[i])
            DFS(i + 1)

            substring.pop()
            DFS(i + 1)

        DFS(0)

        return res
