from collections import deque


def find_root():
    global indegree
    q = deque()
    res = []
    for i in range(1, len(indegree)):
        if not indegree[i]:
            q.append(i)
    while q:
        cur = q.popleft()
        res.append(cur)
        for nxt in singer[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
    if len(res) != N:
        res = 0
    return res


N, M = map(int, input().split())
singer = [[] for _ in range(N + 1)]
for _ in range(M):
    arr = list(map(int, input().split()))[1:]
    for i in range(len(arr) - 1):
        singer[arr[i]].append(arr[i + 1])

indegree = [0] * (N + 1)
for sing in singer:
    for s in sing:
        indegree[s] += 1
l = find_root()
if not l:
    print(l)
else:
    for i in l:
        print(i)