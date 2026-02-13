N = int(input())

arr = []

for _ in range(N):
    a = tuple(map(int, input().split()))
    arr.append(a)

rank_list=  []
for i in range(N):
    rank=1
    for j in range(N):
        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            rank+=1
    rank_list.append(rank)
print(*rank_list)