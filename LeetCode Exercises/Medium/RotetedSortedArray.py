class Solution:
    def findMin(self, nums: List[int]) -> int:

        mid = (len(nums) - 1) // 2
        start = 0
        end = len(nums) - 1

        while (start < end):
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid + 1

            mid = (start + end) // 2

        return nums[start]
