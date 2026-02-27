N, K = map(int, input().split())

vals = [int(input()) for _ in range(N)][::-1]

cnt = 0
for v in vals:
    if K == 0:
        break
    if K >= v:
        cnt += K // v
        K = K % v

print(cnt)