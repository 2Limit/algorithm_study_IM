from collections import deque

def solution(maps):
    answer = -1
    ty = len(maps)
    tx = len(maps[0])
    visited = [[False]*tx for _ in range(ty)]
    visited[0][0]=True
    
    q = deque()
    q.append((0,0,1))
    
    while q:
        cy,cx,cc = q.popleft()
        if cy == ty-1 and cx == tx-1:
            answer = cc
            break
        for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ny = cy+dy
            nx = cx+dx
            if 0 <= ny < ty and 0 <= nx < tx and maps[ny][nx] and not visited[ny][nx]:
                q.append((ny,nx,cc+1))
                visited[ny][nx]=True
    
    
    
    return answer