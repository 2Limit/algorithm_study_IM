T = int(input())

ract = [[0] * 100 for _ in range(100)]
for tc in range(T):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        ract[i][b:b + 10] = [1] * 10
count = 0
for row in ract:
    for i in row:
        if i > 0:
            count += 1
print(count)
