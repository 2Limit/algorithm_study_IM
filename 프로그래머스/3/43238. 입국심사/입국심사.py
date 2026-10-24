def solution(n, times):
    answer = 0
    left = 0
    right = max(times)*n
    
    def possible(mid):
        total = 0
        for t in times:
            total += mid//t
        return total>=n
    
    
    while left<right:
        mid = (left+right)//2
        if not possible(mid):
            left = mid+1
        else :
            right = mid
    answer=left
    
    return answer