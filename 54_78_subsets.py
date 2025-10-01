
# start at the first element
# at each element, we can either go down a path where we add that element to ths subset or go down a path where we dont
# in the end when we've gone through all elements there should be a state where we havent added all elements and that would be the empty set we add to our result
# when we add that element, add it to the current subset and then pop it so we can backtrack 


def subsets(nums):
    res = []
    current_subset = []
    
    # current_subset[:] creates a copy instead of just appending the reference
    
    def backtrack(i):
        # base case: all elements have been added to the current path 
        if i == len(nums):
            res.append(current_subset[:])
            return 
        
        # we do not add it
        
        backtrack(i+1)
        
        # we do add it
        current_subset.append(nums[i])
        backtrack(i+1)
        current_subset.pop()
        
        
    backtrack(0)
    return res
    
        
    


print(subsets(nums = [1,2,3]))