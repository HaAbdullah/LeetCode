# def productExceptSelf(nums):
#     productCounter = dict(nums)
#     return productCounter
        
        
        
        
# Solution 1: Loop through each element, nested loop on rest of the resulting list multiplying it by the current element


def productExceptSelf(nums):
    # res = [1] * len(nums)
    
    # for i in range(len(nums)):
    #     currNum = nums[i]
        
    #     for j in range(len(nums)):
    #         if j != i:
    #             res[j] = res[j] * currNum
    # return res
    
    
    
    
print(productExceptSelf([-1,1,0,-3,3])) 
#print(productExceptSelf([1,2,3,4])) 
#print(productExceptSelf([0,0])) # 0, 0
#print(productExceptSelf([1,0])) # 0, 1
#print(productExceptSelf([4,0,4])) # 0, 0, 0