n = int(input())

dist = list(map(int, input().split()))

cities = list(map(int, input().split()))

buy_val = float('inf')
res = 0
for i in range(len(cities) - 1):
    if buy_val >= cities[i]:
        buy_val = cities[i]
    res += buy_val * dist[i]
print(res)