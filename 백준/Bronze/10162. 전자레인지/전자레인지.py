N = int(input())
div = [0] * 3

a = [300, 60, 10]
for i in range(len(a)):
    div[i] = N // a[i]
    N = N % a[i]
print(*div) if N==0 else print(-1)