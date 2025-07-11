def findMin(nums):
    # if L != R 
    # find mid point
    # if mid point is > RIGHT, its defintely on the right side so you can get rid of left side
        # L = mid +1 
    # if mid point is < RIGHT, its defintely either itself or on the left 
    
    L = 0
    R = len(nums) - 1
    
    while L != R:
        mid = (R + L) // 2
        MID_POINT = nums[mid]
        
        if MID_POINT > nums[R]:
            L = mid + 1 
        else:
            R = mid 
    return nums[L] 