N, M = map(int, input().split())

R = list(map(int, input().split()))
R = set(R[1:]) if len(R) > 1 else 0
res = 0
parties = []
if R:
    for _ in range(M):
        party = set(list(map(int, input().split()))[1:])
        parties.append(party)
        l = party - R
        if l != party:
            R = party | R
            continue
changed = True
while changed:
    changed = False
    for party in parties:
        if party & R:
            if not party <= R:
                R |= party
                changed = True
for p in parties:
    if p == p - R:
        res += 1
if not R:
    res = M
print(res)