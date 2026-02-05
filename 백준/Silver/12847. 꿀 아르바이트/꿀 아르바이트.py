N, X = map(int, input().split())

num_list = list(map(int, input().split()))

window = sum(num_list[:X])
max_pay = window

for i in range(len(num_list) - X):
    window = window - num_list[i] + num_list[i + X]
    max_pay = max(max_pay, window)
print(max_pay)