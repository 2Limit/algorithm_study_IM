import heapq


def dijk(start_idx, end_idx):
    dist = [float('inf')] * (N + 1)
    q = []
    dist[start_idx] = 0
    heapq.heappush(q, (0, start_idx))

    while q:
        cost, cur = heapq.heappop(q)
        if dist[cur] < cost:
            continue
        for point, c in graph[cur]:
            new_cost = cost + c
            if new_cost < dist[point]:
                dist[point] = new_cost
                heapq.heappush(q, (new_cost, point))
    return dist[end_idx]


N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

max_val = -float('inf')
for i in range(1, N + 1):
    a = dijk(i, X)
    b = dijk(X, i)
    max_val = max(max_val, a + b)

print(max_val)