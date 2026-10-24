def solution(land):
    answer = 0
    n=len(land)
    dp = [[0]*4 for _ in range(n)]
    
    dp[0] = land[0][:]
    
    for i in range(1, n):
        prev = dp[i - 1]

        dp[i][0] = land[i][0] + max(prev[1], prev[2], prev[3])
        dp[i][1] = land[i][1] + max(prev[0], prev[2], prev[3])
        dp[i][2] = land[i][2] + max(prev[0], prev[1], prev[3])
        dp[i][3] = land[i][3] + max(prev[0], prev[1], prev[2])
    
    answer  = max(dp[-1])
    return answer