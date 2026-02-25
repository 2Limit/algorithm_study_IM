import heapq

def dijkstra(start):
    dist = [float('inf')] * (N+1)
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))   # (비용, 도시)

    while pq:
        cost, now = heapq.heappop(pq)

        # 이미 더 좋은 경로 있으면 skip
        if dist[now] < cost:
            continue

        for nxt, w in graph[now]:
            new_cost = cost + w

            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))

    return dist


N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
start_point, end_point = map(int, input().split())
visited = [False] * (N + 1)
min_val = float('inf')
print(dijkstra(start_point)[end_point])