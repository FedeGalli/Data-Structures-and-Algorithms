class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        dictionary = {num : -1 for num in nums}

        for num in nums:
            if dictionary.get(num) != -1:
                return True
            else:
                dictionary[num] = num
        
        return False