def productExceptSelf(nums):
    productCounter = dict(nums)
    return productCounter
        
    
print(productExceptSelf([-1,1,0,-3,3])) 
print(productExceptSelf([1,2,3,4])) 
print(productExceptSelf([0,0])) # 0, 0
print(productExceptSelf([1,0])) # 0, 1
print(productExceptSelf([4,0,4])) # 0, 0, 0