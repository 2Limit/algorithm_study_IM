def solution(numbers, target):
    answer = 0
    
    def dfs(a,idx):
        nonlocal answer
        if idx == len(numbers):
            if a == target:
                answer += 1
            return
        dfs(a + numbers[idx], idx + 1)
        dfs(a - numbers[idx], idx + 1)
    dfs(0,0)
    
    
    
    
    return answer