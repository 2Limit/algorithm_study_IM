from collections import deque


def bfs(y, x):
    visited[y][x] = True
    q = deque()
    q.append((y, x, 1))
    while q:
        cy, cx, cc = q.popleft()
        if cy == N - 1 and cx == M - 1:
            return cc

        for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            new_y = cy + dy
            new_x = cx + dx
            if 0 <= new_y < N and 0 <= new_x < M and miro[new_y][new_x] == '1' and not visited[new_y][new_x]:
                visited[new_y][new_x] = True
                q.append((new_y, new_x, cc + 1))


N, M = map(int, input().split())
miro = [input() for _ in range(N)]

visited = [[False] * M for _ in range(N)]

c = bfs(0, 0)
print(c)