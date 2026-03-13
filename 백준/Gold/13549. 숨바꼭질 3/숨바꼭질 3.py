import heapq

N, K = map(int, input().split())


def find():
    dist = [float('inf')] + [float('inf') for _ in range(2 * max(N, K))]
    q = []
    heapq.heappush(q, (N, 0))
    dist[N] = 0

    while q:
        idx, cst = heapq.heappop(q)
        if dist[idx] < cst:
            continue
        dist[idx] = cst
        for i in [-1, 1, 2]:
            if i == -1:
                if 0 <= idx - 1:
                    heapq.heappush(q, (idx - 1, cst + 1))
            elif i == 1:
                if idx + 1 < len(dist):
                    heapq.heappush(q, (idx + 1, cst + 1))
            else:
                if idx * 2 < len(dist) and idx * 2 != 0:
                    heapq.heappush(q, (idx * 2, cst))
    print(dist[K])
find()