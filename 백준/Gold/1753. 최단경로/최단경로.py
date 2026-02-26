import sys

input = sys.stdin.readline
import heapq


def dijk(start_idx):
    dist = [float('inf')] * (V + 1)
    dist[start_idx] = 0
    q = []
    heapq.heappush(q, (0, start_idx))

    while q:
        cost, node = heapq.heappop(q)
        if dist[node] < cost:
            continue
        for next_node, w in graph[node]:
            new_cost = cost + w
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))
    return dist


V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dis = dijk(K)
for s in dis[1:]:
    try:
        print(int(s))
    except:
        print(str(s).upper())
