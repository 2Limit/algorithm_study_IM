N, K = map(int, input().split())
str_list = [x for x in input()]
rule = list(map(int, input().split()))

rule_str = ['A', 'C', 'G', 'T']

window_str = str_list[:K]
window = [0] * 4


def alpha_to_idx(str_list, i):
    return rule_str.index(str_list[i])


for i in window_str:
    idx = rule_str.index(i)
    window[idx] += 1
count = 0

for i in range(N - K+1):
    check = True
    for j in range(len(window)):
        if window[j] < rule[j]:
            check = False
            break
    if check:
        count += 1
    if i == N-K:
        break
    window[alpha_to_idx(str_list, i)] -= 1
    window[alpha_to_idx(str_list, i + K)] += 1

print(count)
