class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i in range(len(nums)):
            if nums[i] not in num_map:
                num_map[nums[i]] = [i]
            else:
                num_map[nums[i]].append(i)

        for elem in num_map:
            if target - elem in num_map:
                if elem == target - elem:
                    if len(num_map[elem]) > 1:
                        return num_map[elem][:2]
                else:
                    return [num_map[elem][0], num_map[target - elem][0]]