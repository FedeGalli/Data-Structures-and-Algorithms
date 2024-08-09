#[0, 6, 2, 1, 5, 16] t = 16
#[0, 1, 2, 5, 10, 16] o(n logn)

def split_in_two(nums):

    nums.sort()
    totalsum = sum(nums)

    if totalsum % 2 == 1:
        return None
    
    totalsum = totalsum / 2
    for num in nums:
        if num > totalsum:
            return None
        else:
            break
    
    reference = len(nums)

    while reference >= 0:
        if nums[reference] <= totalsum:
            break