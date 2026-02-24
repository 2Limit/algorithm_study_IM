def cal(a, b, op):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    else:
        return int(a / b)


def calculator(res, idx):
    global min_val, max_val
    if idx == n:
        if res < min_val:
            min_val = res
        if res > max_val:
            max_val = res
        return

    for i in range(len(ops)):
        if ops[i] == 0:
            continue
        ops[i] -= 1
        calculator(cal(res, nums[idx], i), idx + 1)
        ops[i] += 1

n = int(input())

nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

max_val = -float('inf')
min_val = float('inf')

calculator(nums[0], 1)
print(max_val)
print(min_val)