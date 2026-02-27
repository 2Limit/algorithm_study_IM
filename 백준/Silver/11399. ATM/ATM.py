N = int(input())
nums=sorted(list(map(int,input().split())))
sum_val=0
res=0
for n in nums:
    sum_val+=n
    res+=sum_val
print(res)