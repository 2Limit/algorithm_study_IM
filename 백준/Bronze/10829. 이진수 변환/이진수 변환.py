N = int(input())

result=''
def make_binary(num):
    global result
    if num==0:
        return
    else:
        result+=str(num%2)
        make_binary(num//2)
make_binary(N)
print(result[::-1])