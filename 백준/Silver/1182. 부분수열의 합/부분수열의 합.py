def check(cur,sum,picked):
    if cur==N:
        if sum==S and picked:
            return 1
        else:
            return 0
    pick = check(cur+1,sum+int_list[cur],True)
    skip = check(cur+1,sum,picked)
    return pick+skip


N,S =map(int,input().split())

int_list = list(map(int,input().split()))

print(check(0,0,False))