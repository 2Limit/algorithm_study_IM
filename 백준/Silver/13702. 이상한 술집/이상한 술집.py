N, K = map(int, input().split())
mak = [int(input()) for _ in range(N)]
left = 1
right = max(mak)
while left <= right:
    mid = (left + right) // 2
    count = sum(x // mid for x in mak)
    if count >= K:
        left = mid + 1
    else:
        right = mid - 1
print(right)