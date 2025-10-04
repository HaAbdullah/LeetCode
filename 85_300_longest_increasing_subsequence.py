def lengthOfLIS(nums):

    def dfs(child, parent):
        if child == len(nums):
            return 0 
        
        # option 1: we don't include this child because the next one could be more bigger than it 

        LIS = dfs(child + 1, parent)

        # option 2: child is more than parent 
        if parent == -1 or  nums[parent] < nums[child]:
            LIS = max(LIS, 1 + dfs(child + 1, child))

        return LIS 
    
    return dfs(0, -1)


print(lengthOfLIS([10,9,2,5,3,7,101,18]))