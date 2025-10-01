def partition(s):
    res = []
    n = len(s)
    def backtrack(current_subset,start ):
        if start == n:
            print(f"reached based case adding: {current_subset} ")
            res.append(current_subset[:])
            return 
    
    # check if the current string is a subset 
        # try all possible solutions 
        for end in range(start, n): 
            current_string = s[start:end+1]
            reversed_string = current_string[::-1]
            if current_string == reversed_string:
                print(s[end:n])
                current_subset.append(current_string)
                backtrack(current_subset, end + 1)
                current_subset.pop()

    backtrack([], 0)

    return res


print(partition("aab"))