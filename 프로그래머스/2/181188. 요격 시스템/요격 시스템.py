def solution(targets):
    answer = 0
    
    atk = -float('inf')
    targets.sort(key = lambda x: x[1])
    
    for s, e in targets:
        if s>=atk:
            answer+=1
            atk = e
    
    
    return answer