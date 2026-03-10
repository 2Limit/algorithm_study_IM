from itertools import permutations

N, M = map(int, input().split())
l = sorted(list(map(int, input().split())))
for i in permutations(l, M):
    print(*list(i))