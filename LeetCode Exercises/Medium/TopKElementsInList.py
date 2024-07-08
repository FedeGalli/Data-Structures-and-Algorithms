class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dictionary = {num : 0 for num in nums}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            dictionary[num] += 1

        for num, count in dictionary.items():
            freq[count].append(num)
        
        result = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                result.append(num)
                if (len(result) == k):
                    return result
        

        