import heapq


def solution(jobs):
    n = len(jobs)
    
    tasks = sorted((start,duration,i) for i, (start,duration) in enumerate(jobs))
    heap = []
    time = 0
    idx= 0
    total = 0
    count = 0
    
    while count < n:
        while idx < n and tasks[idx][0] <= time:
            start, duration, job_id  = tasks[idx]
            
            heapq.heappush(heap, (duration,start, job_id))
            idx +=1
            
        if heap:
            duration, start, job_id = heapq.heappop(heap)
            time += duration
            total += time - start
            count +=1
            
        else:
            time = tasks[idx][0]
    
    
    return total // n