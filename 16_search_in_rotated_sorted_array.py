def search(nums, target):
    # have L = 0, R = len(nums) - 1
    # Is M = target? return m 
    
    # check if the right side is in order
    # YES: check if target is between mid and right
        # YES: get rid of the left half
        # NO: get rid of right half 
    
    # NO: check if target > mid or target < right
        #YES: get rid of right half
        #NO: get rid of left half 
    
    L = 0
    R = len(nums) - 1

    while L <= R:
        m = (L + R) // 2
        M = nums[m]

        if M == target:
            return m

        if M < nums[R]:
            if target > M and target <= nums[R]:
                L = m + 1
            else:
                R = m - 1
        else:
            if target < M and target >= nums[L]:
                R = m - 1
            else:
                L = m + 1

    return -1

            
  
print(search(nums = [0,1,2,3,4,5,6], target = 0))          
print(search(nums = [4,5,6,7,0,1,2], target = 0))
print(search(nums = [4,5,6,7,0,1,2], target = 3))
print(search(nums = [1], target = 0))