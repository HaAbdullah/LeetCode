def letterCombinations(digits):
    mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    res = []
    n = len(digits)
    def backtrack(current_combination, i):
        if len(current_combination) == n:
            if current_combination: res.append(current_combination[:])
            return 
        
        for letter in mapping[digits[i]]:
            backtrack(current_combination + letter, i + 1)
        
    backtrack("", 0)

    return res 


print(letterCombinations('23'))
