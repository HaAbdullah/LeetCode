def longestPalindrome(s):
    best_L  = 0
    best_R  = -1
    for i in range(len(s)):
        # center is current letter (odd length palindromes)
        L = i
        R = i 
        while L > -1 and R < len(s) and s[L] == s[R]:
            print(s[L:R+1])
            if (R - L) > (best_R - best_L):
                best_L = L
                best_R = R 
            L -= 1 
            R += 1 
        # center is next space (even length palindromes)
        L = i
        R = i + 1
        while L > -1 and R < len(s) and s[L] == s[R]:
            if (R - L) > (best_R - best_L):
                best_L = L
                best_R = R     
            L -= 1 
            R += 1 

    return s[best_L:best_R+1]

print(longestPalindrome("abxxbabb"))

def longest_palindrome(s: str) -> str:
    # Helper function to check if s[i:j+1] is a palindrome
    def is_palindrome(i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    n = len(s)
    if n == 0:
        return ""

    # dp[i][j] will be True if s[i:j+1] is a palindrome
    dp = [[False] * n for _ in range(n)]
    
    start = 0
    max_len = 1

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check substrings of length 2 and more
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if length == 2:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

            if dp[i][j] and length > max_len:
                start = i
                max_len = length

    return s[start:start + max_len]

# Example usage
string = "babad"
print(longest_palindrome(string))  # Output: "bab" or "aba"
