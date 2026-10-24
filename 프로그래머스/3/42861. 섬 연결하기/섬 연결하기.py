def solution(n, costs):
    parent = list(range(n))
    size = [1]*n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a,b):
        a = find(a)
        b = find(b)
        
        if a == b:
            return False
        
        if size[a]< size[b]:
            a,b = b,a
        
        parent[b]=a
        size[a]+= size[b]
        return True
    
    costs.sort(key = lambda x:x[2])
    count = 0
    answer = 0
    for a,b,cost in costs:
        if union(a,b):
            answer+=cost
            count+=1
            if count == n-1:
                break
    
    
    return answer