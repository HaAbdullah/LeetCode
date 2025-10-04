def numDecodings(s):
    map = {
    "1": "A",
    "2": "B",
    "3": "C",
    "4": "D",
    "5": "E",
    "6": "F",
    "7": "G",
    "8": "H",
    "9": "I",
    "10": "J",
    "11": "K",
    "12": "L",
    "13": "M",
    "14": "N",
    "15": "O",
    "16": "P",
    "17": "Q",
    "18": "R",
    "19": "S",
    "20": "T",
    "21": "U",
    "22": "V",
    "23": "W",
    "24": "X",
    "25": "Y",
    "26": "Z"
    }
    
    def dfs(start, end):
        if map.get(s[start:end], -1) == -1:
            return 0 
        if end == len(s):
            return 1 
        return dfs(end, end + 1) + dfs(start, end + 1)

    
    return dfs(0, 1)

def numDecodings(s):
    map = {str(i): chr(64 + i) for i in range(1, 27)}
    memo = {}
    
    def dfs(start, end):
        # Check memo first
        if (start, end) in memo:
            return memo[(start, end)]
        
        if map.get(s[start:end], -1) == -1:
            return 0 
        if end == len(s):
            return 1 
        
        # Calculate result and store in memo
        result = dfs(end, end + 1) + dfs(start, end + 1)
        memo[(start, end)] = result
        return result
    
    return dfs(0, 1)


def numDecodings(s):
    n = len(s)

    if len(s) ==  0: return 0
    dp = [0] * (n + 1)
    dp[n] = 1

    for i in range(n - 1, -1 , -1):
        # Recurrence relation: dp[i] = dp[i+1] + dp[i+2]

        if s[i] != '0':
            dp[i] += dp[i + 1]
        # Check 2-digit decode
        if i + 1 < n:
            two_digit = s[i:i+2]
            if 10 <= int(two_digit) <= 26:
                dp[i] += dp[i + 2]
    
    return dp[0]
print(numDecodings("12"))