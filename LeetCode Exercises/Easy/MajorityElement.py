class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        supDic = {}

        for num in nums:
            if supDic.get(num, None) == None:
                supDic[num] = 1
            
            else:
                supDic[num] += 1
                
            if supDic[num] > len(nums) / 2:
                return num
        
