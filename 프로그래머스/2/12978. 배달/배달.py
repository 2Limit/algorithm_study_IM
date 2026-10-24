import heapq

def solution(N, road, K):
    answer = 0
    
    
    def dijk(s):
        dist = [float('inf')]*(N+1)
        dist[s]=0
        q = []
        heapq.heappush(q,(0,s))
        
        while q:
            cost, node = heapq.heappop(q)

            for s_node,e_node,w in road:
                if s_node == node or e_node == node:
                    new_cost = cost+w
                    if new_cost < dist[e_node]:
                        dist[e_node]=new_cost
                        heapq.heappush(q,(new_cost,e_node))
                    if new_cost < dist[s_node]:
                        dist[s_node]=new_cost
                        heapq.heappush(q,(new_cost,s_node))
        return dist                    
    
    dist = dijk(1)
    
    for d in dist:
        if d <=K:
            answer+=1
    print(dist)
    return answer