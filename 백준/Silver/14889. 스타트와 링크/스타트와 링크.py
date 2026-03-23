from itertools import combinations


def team_point(iter):
    sum_val = 0
    for y, x in combinations(iter, 2):
        sum_val += mat[y][x]
        sum_val += mat[x][y]
    return sum_val


def make_team():
    nums = [x for x in range(N)]
    all_combs = list(combinations(nums, N // 2))
    res = float('inf')
    for comb in all_combs[:len(all_combs) // 2]:
        A = set(comb)
        B = set(nums) - A
        a_point = team_point(A)
        b_point = team_point(B)
        res = min(res, abs(a_point - b_point))
    return res


N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

ans = make_team()
print(ans)