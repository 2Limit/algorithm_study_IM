T = int(input())

# 1,2,3의 정수들만을 사용해서 더했을 때, num을 만들 수 있는 가지 수
# 현재 위치에서 도착점 num까지
def check(cur):
    if cur==0:
        return 1
    elif cur<0:
        return 0
    return check(cur-1)+check(cur-2)+check(cur-3)


for _ in range(T):
    n = int(input())
    print(check(n))