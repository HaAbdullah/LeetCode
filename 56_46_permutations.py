def permute(nums):
    res = []
    def backtrack(current_permutation, current_available):
        if len(current_permutation) == len(nums):
            res.append(current_permutation[:])
            return 
        
        for i in range(len(current_available)):
            current_permutation.append(current_available[i])
            # remove chosen element from the pool
            backtrack(current_permutation, current_available[:i] + current_available[i+1:])
            current_permutation.pop()

    backtrack([], nums)
    return res 

print(permute([1,2,3]))


class Solution:
    def permute(nums):
        if len(nums) == 0:
            return [[]]

        perms = permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res