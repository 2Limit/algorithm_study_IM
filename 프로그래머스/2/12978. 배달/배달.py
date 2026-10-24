import heapq

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N + 1)]
    
    for s,e,w in road:
        graph[s].append((e,w))
        graph[e].append((s,w))
    
    
    def dijk(s):
        dist = [float('inf')]*(N+1)
        dist[s]=0
        q = []
        heapq.heappush(q,(0,s))
        
        while q:
            cost, node = heapq.heappop(q)
                
            if cost > dist[node]:
                continue
            for e_node,w in graph[node]:
                new_cost = cost+w
                if new_cost < dist[e_node]:
                    dist[e_node]=new_cost
                    heapq.heappush(q,(new_cost,e_node))
            
        return dist                    
    
    dist = dijk(1)
    for d in dist:
        if d<=K:
            answer+=1
    return answer