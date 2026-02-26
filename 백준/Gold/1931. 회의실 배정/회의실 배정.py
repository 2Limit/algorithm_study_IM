N = int(input())

conf = []
start_min = 0
end_max = 0
for _ in range(N):
    a, b = map(int, input().split())
    conf.append((a, b))

conf.sort(key=lambda x: (x[1], x[0]))
end = 0
cnt = 0
for a in conf:
    if end <= a[0]:
        end = a[1]
        cnt += 1
print(cnt)