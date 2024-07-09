class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(numbers[:len(numbers) - 1]):
            for j, num2 in enumerate(numbers[1:]):
                if num1 + num2 > target:
                    break
                
                if num1 + num2 == target:
                    return [i + 1, j + 2]
