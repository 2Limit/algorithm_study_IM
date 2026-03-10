a, b, c = map(int, input().split())


def power(a, b):
    if b == 1:
        return a % c

    half = power(a, b // 2)

    if b % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c


l = power(a, b)
print(l)
