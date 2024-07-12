import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        
        return 2 ** round(math.log(abs(n), 2)) == n