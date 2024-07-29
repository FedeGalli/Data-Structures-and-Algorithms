class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer = []


        for i in range(len(nums)):
            if i == 0:
                answer.append(1)
            else:
                answer.append(answer[i - 1] * nums[i - 1])

        current = 1
        for i in range(len(nums) - 1, -1, -1):
            
            answer[i] *= current
            current *= nums[i]

        
        return answer