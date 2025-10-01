def combinationSum2(candidates, target):

    res = []
    candidates.sort()
    def backtrack(current_sum, current_combination, i):
        if current_sum == target:
            res.append(current_combination[:])
            return
        if i == len(candidates) or current_sum > target:
            return 
        
        # option 1: move to the next element (might be a duplicate)
        current_combination.append(candidates[i])
        backtrack(current_sum + candidates[i], current_combination, i + 1)
        current_combination.pop()
        # option 2: skip next element and all duplicates 
        while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
            i += 1 
        backtrack(current_sum, current_combination, i + 1)
        
    backtrack(0, [], 0)

    return res 

print(combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))