arr = []
for _ in range(9):
    ki = int(input())
    arr.append(ki)
result=[]

for i in range(1<< len(arr)):
    sum_val=[]
    for j in range(len(arr)):
        if i & (1<<j):
            sum_val.append(arr[j])
    if sum(sum_val)==100 and len(sum_val)==7:
        result=sum_val
        break

result= sorted(result)
for s in result:
    print(s)