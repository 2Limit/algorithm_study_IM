from collections import deque


def bfs():
    q = deque()
    q.append((0, 0, 1, 0))
    visited[0][0][0] = True

    while q:
        y, x, dist, wall = q.popleft()

        if y == N - 1 and x == M - 1:
            return dist

        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny = y + dy
            nx = x + dx

            if 0 <= ny < N and 0 <= nx < M:

                # 길
                if mat[ny][nx] == 0 and not visited[ny][nx][wall]:
                    visited[ny][nx][wall] = True
                    q.append((ny, nx, dist + 1, wall))

                # 벽
                if mat[ny][nx] == 1 and wall == 0:
                    visited[ny][nx][1] = True
                    q.append((ny, nx, dist + 1, 1))

    return -1


N, M = map(int, input().split())

mat = [[0] * M for _ in range(N)]

for i in range(N):
    st = input()
    for j in range(len(st)):
        a = int(st[j])
        if a:
            mat[i][j] = a
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
res = float('inf')
a = bfs()
if a != -1:
    res = min(res, a)
print(res) if res != float('inf') else print(-1)