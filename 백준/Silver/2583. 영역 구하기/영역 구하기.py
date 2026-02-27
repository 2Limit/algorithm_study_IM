import sys
sys.setrecursionlimit(10000)
M, N, K = map(int, input().split())
mat = [[False] * N for _ in range(M)]
for _ in range(K):
    sx, sy, ex, ey = map(int, input().split())
    for i in range(sy, ey):
        for j in range(sx, ex):
            if not mat[i][j]:
                mat[i][j] = True

areas = []


def dfs(y, x):
    global ar
    if not mat[y][x]:
        mat[y][x] = True
        ar += 1

    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_y = y + dy
        new_x = x + dx
        if 0 <= new_y < M and 0 <= new_x < N:
            if not mat[new_y][new_x]:
                dfs(new_y, new_x)



for i in range(len(mat)):
    for j in range(len(mat[i])):
        if not mat[i][j]:
            ar = 0
            dfs(i, j)
            areas.append(ar)
print(len(areas))
print(*sorted(areas))