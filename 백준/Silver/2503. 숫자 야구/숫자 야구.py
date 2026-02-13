def check(a, b):
    a_list = list(str(a))
    b_list = list(str(b))
    b_set = set(b_list)
    strike = 0
    ball = 0
    if len(b_set)!=3:
        return -1,-1
    if '0' in b_list:
        return -1,-1
    for i in range(3):
        if a_list[i] == b_list[i]:
            strike += 1
        elif a_list[i] in b_list:
            ball += 1
    return strike, ball


count = 0

N = int(input())
count = 0
inp_list = [list(map(int, input().split())) for _ in range(N)]

for i in range(100, 1000):
    mini_count = 0
    for inp in inp_list:
        num = inp[0]
        strike = inp[1]
        ball = inp[2]

        a, b = check(num, i)
        if a == strike and b == ball:
            mini_count += 1
    if mini_count == N:
        count += 1
print(count)