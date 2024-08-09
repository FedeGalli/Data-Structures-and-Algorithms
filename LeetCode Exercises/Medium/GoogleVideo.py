#[1, 2, 3, 9] s=8
#[1, 2, 4, 4] s=8

def findPair(nums, s):
    res = []
    map = {}
    for num in nums:
        if s - num in map:
            res.append([num, s - num])
            map[num] = 1
        else:
            map[num] = 1
        
    return res


print(findPair([1, 2, 3, 4, 4, 5, 9], 8))