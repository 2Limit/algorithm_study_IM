N = 1000 - int(input())

div = [500, 100, 50, 10, 5, 1]
res = 0
for d in div:
    if N==0:
        break
    res+=(N//d)
    N%=d
print(res)