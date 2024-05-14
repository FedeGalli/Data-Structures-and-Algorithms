"""
Do not return anything, modify nums1 in-place instead.
"""
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        if m == 0:
            nums1 = nums2
            return
        if n == 0:
            return
        j = 0
        for i in range(m + n):
            if (nums1[i] == 0 and i >= m + j ):
                nums1[i] = nums2[j]
                j += 1
            elif (nums2[j] < nums1[i]):
                #shift the array
                prev = nums1[i]
                curr = 0
                for k in range(i + 1, m + n):
                    curr = nums1[k]
                    nums1[k] = prev
                    prev = curr
                    
                
                nums1[i] = nums2[j]
                
                j += 1
            print(nums1)
            print(i)


ciao = Solution()

ciao.merge([1, 2, 3, 0, 0, 0], 3, [2,5,6], n = 3)