import sys
input = sys.stdin.readline


def dp_():
    dp[0][1] = mat[0][0]
    dp[0][2] = mat[1][0]
    for i in range(1, N):
        dp[i][0] = max(dp[i][0], max(dp[i - 1]))
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + mat[0][i]
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + mat[1][i]
    return max(dp[-1])


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * 3 for _ in range(N)]
    ans = dp_()
    print(ans)