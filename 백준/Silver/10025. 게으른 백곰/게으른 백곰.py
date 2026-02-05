N, K = map(int, input().split())
nums = [0] * 1000000
for _ in range(N):
    a, b = map(int, input().split())
    nums[b] = a
max_ice = 0

if 2 * K >= len(nums):
    max_ice = sum(nums)
else:
    window = sum(nums[0:2 * K])
    max_ice = 0
    for i in range(K, len(nums) - K):
        window = window - nums[i - K-1] + nums[i + K]
        if max_ice < window:
            max_ice = max(max_ice, window)
print(max_ice)