def rob(nums):
    L = nums[0]
    R = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        new = max(R, L + nums[i])
        L = R 
        R = new 
    return new
print(rob([2,7,9,3,1]))