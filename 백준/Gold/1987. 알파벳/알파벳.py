import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

R, C = map(int, input().split())
mat = [input().strip() for _ in range(R)]

visited = set()
res = 0

def dfs(y, x, mask, depth):
    global res
    res = max(res, depth)

    if (y, x, mask) in visited:
        return
    visited.add((y, x, mask))

    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
        ny, nx = y + dy, x + dx

        if 0 <= ny < R and 0 <= nx < C:
            bit = 1 << (ord(mat[ny][nx]) - 65)

            if mask & bit:
                continue

            dfs(ny, nx, mask | bit, depth + 1)

start = 1 << (ord(mat[0][0]) - 65)
dfs(0, 0, start, 1)

print(res)