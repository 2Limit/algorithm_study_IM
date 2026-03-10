v = list(map(int, input().split()))
h = list(map(int, input().split()))

score = [6, 3, 2, 1, 2]

visitor = sum(v[i] * score[i] for i in range(5))
home = sum(h[i] * score[i] for i in range(5))

print(visitor, home)