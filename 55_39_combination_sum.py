# DISTINCT INTEGERS: candidates 
# target integer

# [2,3,6,7] and target = 7
def combinationSum(candidates, target):
    
    res = []
    current_combination = []
    current_sum = 0
    n = len(candidates)
    def backtrack(start):
        nonlocal current_combination
        nonlocal current_sum
        nonlocal res
        if current_sum == target:
            res.append(current_combination[:])
            return 
        
        # try all numbers in this current level
        
        for i in range(start, n):
            current_sum += candidates[i]
            if current_sum <= target:
                current_combination.append(candidates[i])
                backtrack(i)
                current_combination.pop()
            current_sum -= candidates[i]
                
        
    backtrack(0)
    return res 
        
        
        
print(combinationSum(candidates = [2,3,6,7], target = 7))