def countSubstrings(s):
    count = 0 
    for i in range(len(s)):
        # start at the character (odd length palindrome)
        L, R = i, i 
        while L >= 0 and R < len(s) and s[L] == s[R]:
            # is a palindrome! 
            L -= 1 
            R += 1
            count += 1  
        # start at the space after character (even length palindrome)
        L, R = i, i + 1 
        while L >= 0 and R < len(s) and s[L] == s[R]:
            # is a palindrome! 
            L -= 1 
            R += 1
            count += 1 

    return count 
#print(countSubstrings("aaaaaa"))

def countSubstrings(s):
    count = 0 
    dp = [[-1 for i in range(len(s))] for i in range(len(s))]
    def isPalindrome(i, j):
        nonlocal dp 
        while i < j:
            if s[i] != s[j]: 
                dp[i][j] = False
                return False
            i += 1
            j -= 1
        dp[i][j] = True
        return True  

    for i in range(len(s)):
        for j in range(i, len(s)):
            if dp[i][j] == False:
                continue 
            if dp[i][j] == True:
                count += 1
                continue 
            if isPalindrome(i, j):
                count += 1 
    return count

#print(countSubstrings("abc"))


def countSubstrings(s):
    dp = [[False for i in range(len(s))] for i in range(len(s))]
    n = len(s)
    res = 0
    for i in range(n - 1, -1, -1): 
        for j in range(i, n):
            if s[i] == s[j] and (j - i <= 2 or dp [i+1][j-1]):
                dp[i][j] = True
                res += 1 
    return res
print(countSubstrings("abcd"))
