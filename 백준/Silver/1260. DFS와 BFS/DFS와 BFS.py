from collections import deque

N,M,V =map(int,input().split())

graph=[[] for _ in range(N+1)]


# 그래프
for _ in range(M):
    start,end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)


used=[0]*(N+1)
def dfs(start):
    print(start,end=' ')
    used[start] = 1
    # start에서 갈 수 있는 지점 작은 수로 정렬
    # 경로 작은 수 부터 탐색
    graph[start]=sorted(graph[start])
    for next_node in graph[start]:
        # 방문한 적 없나요?
        if not used[next_node]:
            dfs(next_node)
        used[next_node]=1
    return

def bfs(start):
    # deque 시작점 넣고 시작
    dq = deque([start])
    # 방문 초기 값
    visited = [0] * (N + 1)
    visited[start] = 1
    print(start,end=' ')

    # dq에 다음 길이 없을 때까지
    while dq:
        now = dq.popleft()
        # 갈 수 있는 경로 탐색
        graph[now]=sorted(graph[now])
        for next_node in graph[now]:
            # 방문했나요?
            if visited[next_node]:
                continue
            print(next_node, end=' ')
            visited[next_node]=1
            dq.append(next_node)

            
dfs(V)
print()
bfs(V)