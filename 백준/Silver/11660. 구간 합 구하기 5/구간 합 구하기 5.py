import sys
input = sys.stdin.readline

N, M = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]

a = [list(map(int, input().split())) for _ in range(M)]

S = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        S[i][j] = (
            S[i-1][j]
            + S[i][j-1]
            - S[i-1][j-1]
            + mat[i-1][j-1]
        )
for x1, y1, x2, y2 in a:
    ans = (
            S[x2][y2]
            - S[x1 - 1][y2]
            - S[x2][y1 - 1]
            + S[x1 - 1][y1 - 1]
    )
    print(ans)