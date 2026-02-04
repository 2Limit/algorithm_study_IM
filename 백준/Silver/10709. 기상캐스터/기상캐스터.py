H, W = map(int, input().split())
str_mat = [[x for x in input()] for _ in range(H)]

for s in str_mat:
    delta = []
    now_delta = -1
    for i in range(len(s)):
        if s[i] == 'c':
            now_delta = 0
        elif now_delta != -1:
            now_delta += 1
        delta.append(now_delta)
    print(*delta)