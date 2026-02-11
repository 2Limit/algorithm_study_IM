# 시작점! result=''?
# 엔드포인트! len(result)==len(N)
def dfs(result,list):
    # 앞에 자르던게 N의 앞부분보다 작다면 잘라라!
    if result != '' and int(result) < int(N[:len(result)]):
        return
    # 종단점
    if len(result) == len(N) and result not in int_list:
        if int(result) == int(N):
            return
        int_list.append(result)
        return
    for i in range(len(list)):
        result += list[0]
        a = list.pop(0)
        dfs(result,list)
        list.append(a)
        result = result[:len(result) - 1]


N = input()
n = int(''.join(N))
int_list = []
dfs('',list(N))
print(min(list(map(int, int_list)))) if len(int_list) != 0 else print(0)
