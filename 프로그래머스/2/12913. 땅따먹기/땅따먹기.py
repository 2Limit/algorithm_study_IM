def solution(land):
    answer = 0
    n=len(land)
    prev = land[0][:]
    
    for i in range(1, n):
        curr = [0]*4

        curr[0] = land[i][0] + max(prev[1], prev[2], prev[3])
        curr[1] = land[i][1] + max(prev[0], prev[2], prev[3])
        curr[2] = land[i][2] + max(prev[0], prev[1], prev[3])
        curr[3] = land[i][3] + max(prev[0], prev[1], prev[2])
        
        prev = curr
    answer  = max(prev)
    return answer