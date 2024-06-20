#A child is running up a staircase with n steps and can hop either 1, 2 or 3 steps at a time. Implement a method
#to count how many possible ways the child can run up the stairs.

'''
def countWays(n : int) -> int:
    if (n < 0):
        return 0
    if (n == 0):
        return 1

    return countWays(n - 1) + countWays(n - 2) + countWays(n - 3)
'''

#solution with dynamic programming

def countWaysa (n : int) -> int:
    buffer = [-1] * (n + 1)
    return countWays(n, buffer)

def countWays(n : int, buffer) -> int:
    if (n < 0):
        return 0
    if (n == 0):
        return 1
    
    if (buffer[n] == -1):
        buffer[n] = countWays(n - 1, buffer) + countWays(n - 2, buffer) + countWays(n - 3, buffer)

    return buffer[n]

print(countWaysa(3))