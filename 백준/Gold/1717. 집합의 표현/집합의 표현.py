import sys

sys.setrecursionlimit(10**6)
n, m = map(int, input().split())

parent = [i for i in range(n + 1)]


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    a = find(x)
    b = find(y)
    if a != b:
        parent[a] = b

for _ in range(m):
    a,b,c = map(int, input().split())
    if not a:
        union(b,c)
    else :
        if find(b) == find(c):
            print('YES')
        else:
            print('NO')