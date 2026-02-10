T = int(input())

for _ in range(T):
    W = input()
    K = int(input())
    count_list = {x:W.count(x) for x in W }
    v_list = [k for k in count_list if count_list[k]>=K]
    if len(v_list)==0:
        print(-1)
        continue
    diff_list=[]
    for v in v_list:
        v_idx_list = [i for i,x in enumerate(W) if x==v]
        for i in range(len(v_idx_list)-K+1):
            diff= max(v_idx_list[i:i+K])-min(v_idx_list[i:i+K])
            diff_list.append(diff)

    print(min(diff_list)+1,max(diff_list)+1)