N , M  = map(int,input().split())

arr = [x+1 for x in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    arr[a-1:b]=reversed(arr[a-1:b])

print(*arr)