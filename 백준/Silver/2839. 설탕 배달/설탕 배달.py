N = int(input())
res = -1
n = N // 5
for i in range(n, 0, -1):
    if (N - (5 * i)) % 3 == 0:
        res = i + (N - (5 * i)) // 3
        break
if res==-1 and N % 3 == 0:
    res = N // 3
print(res)