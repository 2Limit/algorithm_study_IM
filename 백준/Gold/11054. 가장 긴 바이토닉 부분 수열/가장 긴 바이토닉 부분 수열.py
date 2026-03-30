import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

bi_dp = [1] * n

for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if arr[j] < arr[i]:
            bi_dp[i] = max(bi_dp[i], bi_dp[j] + 1)
result = 0
for i in range(n):
    result = max(result, dp[i] + bi_dp[i] - 1)

print(result)