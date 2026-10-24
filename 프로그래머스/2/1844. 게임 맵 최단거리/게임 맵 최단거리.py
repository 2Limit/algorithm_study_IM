from collections import deque


def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]

    q = deque()
    q.append((0,0,1))
    visited[0][0]=True
    while q:
        cy,cx,cc = q.popleft()
        if cy == n-1 and cx == m-1:
            answer = cc
            break
        
        for dy,dx in ([0,1],[0,-1],[1,0],[-1,0]):
            ny = cy+dy
            nx = cx+dx
            if 0<=ny<n and 0<=nx<m and maps[ny][nx] and not visited[ny][nx]:
                visited[ny][nx]=True
                q.append((ny,nx,cc+1))
      

    return answer
