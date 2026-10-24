def solution(routes):
    routes.sort(key=lambda x: x[1])
    
    answer = 0
    cam = float('-inf')
    
    for s,e in routes:
        if s>cam:
            answer +=1
            cam = e
    
    return answer