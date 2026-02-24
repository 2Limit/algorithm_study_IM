import heapq

N = int(input())
nums = []
for _ in range(N):
    heapq.heappush(nums, int(input()))

res = 0
while len(nums) > 1:
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    s = a + b
    res += s
    heapq.heappush(nums, s)

print(res)