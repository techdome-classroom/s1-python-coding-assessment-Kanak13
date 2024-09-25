def matches(secret, pattern):
    m, n = len(secret), len(pattern)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
   
    
    dp[0][0] = True
   
    
    for j in range(1, n + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[j - 1] == secret[i - 1] or pattern[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

    return dp[m][n]


print(matches("aa", "a"))      
print(matches("aa", "*"))      
print(matches("cb", "?a"))    
print(matches("adceb", "*a*b"))

