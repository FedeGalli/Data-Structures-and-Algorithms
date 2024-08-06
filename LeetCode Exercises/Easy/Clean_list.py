def clean_list(nums):
    
    p1 = 0
    p2 = 1
    
    while(p2 < len(nums)):
        
        if nums[p1] == 0:
            while(p2 < len(nums)):
                if nums[p2] != 0:
                    nums[p1] = nums[p2]
                    nums[p2] = 0
                    break
                
                p2 += 1
            
        p1 += 1
        p2 += 1
        
    
    return nums