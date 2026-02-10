N = int(input())
mod = 1000000007
fibo = [0] * 1000001
fibo[0] = 0  # 초기값
fibo[1] = 1  # 초기값

# 세 번째 수부터는 이전의 값들을 활용할 수 있다
for i in range(2, 1000001):
    fibo[i] = (fibo[i-1] + fibo[i-2]) % mod

print(fibo[N])