class Solution:
    def isThree(self, n: int) -> bool:
        div = 0
        
        for i in range(1, n+1, 2):
            if n % 2 == 0:
                div += 1
            if n % i == 0:
                div += 1
            if div > 3:
                return False


        if div == 3:
            return True

        return False
