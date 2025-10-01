def combinationSum2(candidates, target):
    res = []
    current_combination = []
    candidates.sort()  # Sort first!
    
    def backtrack(start, current_sum):
        if current_sum == target:
            res.append(current_combination[:])
            return 
        
        for i in range(start, len(candidates)):
            # Skip duplicates: if this isn't the first element at this level
            # and it's the same as the previous element
            if i > start and candidates[i] == candidates[i-1]:
                continue
                
            if current_sum + candidates[i] > target:
                break  # Optimization: since sorted, no point continuing
                
            current_combination.append(candidates[i])
            backtrack(i+1, current_sum + candidates[i])
            current_combination.pop()
    
    backtrack(0, 0)
    return res

print(combinationSum2([10,1,2,7,6,1,5], 8))