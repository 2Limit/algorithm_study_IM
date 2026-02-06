N, M = map(int, input().split())

basket = [0] * N
for _ in range(M):
    start, end, ball = map(int, input().split())
    start = start - 1
    basket[start:end] = [ball for x in basket[start:end]]

print(*basket)