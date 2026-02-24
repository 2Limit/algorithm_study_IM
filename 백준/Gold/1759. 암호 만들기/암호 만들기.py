L, C = map(int, input().split())
alphas = input().split()
alphas.sort()


def password(start_idx, s):
    if len(s) > 1:
        for i in range(1, len(s)):
            if ord(s[i - 1]) > ord(s[i]):
                return
    if len(s) == L:
        v = 0
        for c in s:
            if c in 'aeiou':
                v += 1
        if v >= 1 and len(s) - v >= 2:
            print(s)
    for i in alphas[start_idx:]:
        if i in s:
            continue
        password(start_idx + 1, s + i)


password(0, '')