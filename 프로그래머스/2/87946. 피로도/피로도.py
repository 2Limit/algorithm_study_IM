def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    def dfs(mask,c,d):
        nonlocal answer
        answer = max(answer,d)
        for i in range(n):
            if mask & (1<<i):
                continue
            if k-c < dungeons[i][0]:
                continue
            next_mask = mask | (1<<i)
            dfs(next_mask,c+dungeons[i][1],d+1)
            
    
    dfs(0,0,0)
    
    return answer