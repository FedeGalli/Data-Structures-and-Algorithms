class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]

        for i in range(1, len(nums)):
            
            if curr_sum + nums[i] < nums[i]:
                curr_sum = nums[i]
                if nums[i] > max_sum:
                    max_sum = nums[i]
            else:
                if curr_sum + nums[i] >= max_sum:
                    max_sum = curr_sum + nums[i]

                curr_sum += nums[i]
        
        return max_sum