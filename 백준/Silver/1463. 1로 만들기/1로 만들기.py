N = int(input())

# dp[x] = x를 1로 만드는 최소 연산 횟수
dp = [0] * (N + 1)

for i in range(2, N + 1):
    # 1 빼기 연산
    dp[i] = dp[i - 1] + 1

    # 2로 나누기 가능하면 비교
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    # 3으로 나누기 가능하면 비교
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])