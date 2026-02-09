N = int(input())

def pibo(num):

    if num==0:
        return 0
    elif num<=2:
        return 1
    else :
        return pibo(num-1)+pibo(num-2)
print(pibo(N))