class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}


        for num in nums:
            if dic.get(num, None) == None:
                dic[num] = num
            else:
                del dic[num]

        return list(dic.values())[0]
        