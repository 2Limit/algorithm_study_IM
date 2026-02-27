tc = 0
while True:
    tc += 1
    res = 0
    L, P, V = map(int, input().split())
    if L == 0 and V == 0 and P == 0:
        break
    res += ((V // P) * L)
    res += (L if V%P>=L else V%P)

    print(f'Case {tc}: {res}')