from collections import deque


def count_zero(temp):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not temp[i][j]:
                cnt += 1
    return cnt


def virus(temp):
    q = deque()

    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                q.append((i, j))

    while q:
        y, x = q.popleft()

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny = y + dy
            nx = x + dx

            if 0 <= ny < N and 0 <= nx < M and temp[ny][nx] == 0:
                temp[ny][nx] = 2
                q.append((ny, nx))


def make_wall(cnt):
    global ans

    if cnt == 3:
        temp = [row[:] for row in mat]

        virus(temp)

        ans = max(ans, count_zero(temp))
        return

    for i in range(N):
        for j in range(M):

            if mat[i][j] == 0:
                mat[i][j] = 1
                make_wall(cnt + 1)
                mat[i][j] = 0


N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
ans = -float('inf')
make_wall(0)
print(ans)