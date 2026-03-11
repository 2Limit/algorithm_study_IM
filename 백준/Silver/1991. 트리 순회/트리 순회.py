def in_ord(s):
    l, r = tree.get(s)

    print(s, end='')
    if l.isalpha():
        in_ord(l)
    if r.isalpha():
        in_ord(r)


def mid_ord(s):
    l, r = tree.get(s)

    if l.isalpha():
        mid_ord(l)
    print(s, end='')
    if r.isalpha():
        mid_ord(r)


def out_ord(s):
    l, r = tree.get(s)

    if l.isalpha():
        out_ord(l)
    if r.isalpha():
        out_ord(r)
    print(s, end='')


N = int(input())

tree = {}

for _ in range(N):
    parent, left, right = input().split()
    tree[parent] = (left, right)
in_ord('A')
print()
mid_ord('A')
print()
out_ord('A')