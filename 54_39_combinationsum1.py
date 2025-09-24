def combinationSum(candidates, target):
    res = []
    def backtrack(current_combination, current_sum, i):
        if current_sum == target:
            res.append(current_combination[:])
            return 
        if i == len(candidates) or current_sum > target: 
            return 
        
        # option 1: add another of the same element
        current_combination.append(candidates[i])
        backtrack(current_combination, current_sum + candidates[i], i ) # don't need to subtract because you're just passing in an added version, when it returns current_sum will still have the original value 
        current_combination.pop()
        # option 2: move on to the next element 
        backtrack(current_combination, current_sum, i + 1)

    backtrack([], 0, 0)
    return res 

print(combinationSum(candidates = [2,5,6,9], target = 9))