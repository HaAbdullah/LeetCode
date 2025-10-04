# s = boldat
# dictionarywords = [bol, bold, at]

def wordBreak(s, wordDict):
    wordDict = set(wordDict)
    dp = [[False for i in range(len(s) + 1)] for i in range(len(s) + 1)]
    

    for i in range(len(s), -1, -1):
        for j in range(i, len(s) + 1):
            if i == j:
                dp[i][j] = True
            elif s[i:j] in wordDict:
                dp[i][j] = dp[j][j] or dp[j][len(s)]  # word found, check rest
            
            if j < len(s):
                dp[i][len(s)] = dp[i][len(s)] or dp[i][j]

    return dp[0][len(s)]
print(wordBreak(s="leetcode", wordDict=["leet","code"]))

