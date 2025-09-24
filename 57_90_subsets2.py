def subsetsWithDup(nums):
    nums.sort()
    n = len(nums)
    res = []
    def backtrack(current_subset, i):
        if i == n:
            res.append(current_subset[:])
            return 
        
        # option 1: add the current element 
        current_subset.append(nums[i])
        backtrack(current_subset, i + 1)
        current_subset.pop()
        
        # option 2: skip the current element and all instances of the current element 
        while i < len(nums) - 1 and nums[i] == nums[i+1]:
            i += 1 

        backtrack(current_subset, i + 1)
    
    backtrack([], 0)
    return res


print(subsetsWithDup([1,2,2]))