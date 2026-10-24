def solution(sequence, k):
    answer = []
    
    left = 0
    total = 0
    min_len = float('inf')
    
    for right in range(len(sequence)):
        total += sequence[right]
        while total > k:
            total -= sequence[left]    
            left +=1
        if total == k:
            length = right - left +1
            if length < min_len :
                min_len = length
                answer = [left,right]
    
    
    return answer