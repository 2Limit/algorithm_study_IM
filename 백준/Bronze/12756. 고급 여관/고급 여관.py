a_a, a_h = map(int, input().split())
b_a, b_h = map(int, input().split())

while a_h > 0 and b_h > 0:
    a_h -= b_a
    b_h -= a_a

if a_h <= 0:
    if b_h <= 0:
        print('DRAW')
    else:
        print('PLAYER B')
else:
    print('PLAYER A')
