import sys
import heapq

input = sys.stdin.readline

N = int(input())
nums = []

for _ in range(N):
    a = int(input())
    if a == 0:
        if not nums:
            print(0)
        else:
            print(-heapq.heappop(nums))
    else:
        heapq.heappush(nums, -a)