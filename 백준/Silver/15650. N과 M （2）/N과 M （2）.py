from itertools import combinations

N, M = map(int, input().split())
l = [x for x in range(1, N + 1)]
for i in combinations(l, M):
    print(*list(i))