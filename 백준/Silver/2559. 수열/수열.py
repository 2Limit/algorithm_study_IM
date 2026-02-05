N, K = map(int, input().split())

tmp_list = list(map(int, input().split()))

window = sum(tmp_list[:K])

max_tmp = window
for i in range(N - K):
    window = window - tmp_list[i] + tmp_list[i + K]
    max_tmp = max(max_tmp, window)
print(max_tmp)
