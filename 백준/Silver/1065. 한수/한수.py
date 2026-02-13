N = input()
n=int(N)

count =0
for i in range(1,n+1):
    if i<=9:
        count+=1
        continue
    elif i<=99:
        count+=1
        continue
    elif i>=100 :
        hansu=True
        I = str(i)
        for j in range(1,len(I)-1):
            if int(I[j])-int(I[j-1])!=int(I[j+1])-int(I[j]):
                hansu=False
                break
        if hansu:
            count+=1
print(count)