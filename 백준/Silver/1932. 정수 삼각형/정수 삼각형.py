def dp():
    sum_graph[0][0] = graph[0][0]
    for i in range(1, N):
        for j in range(len(graph[i])):
            if j == 0:
                sum_graph[i][j] = sum_graph[i - 1][j] + graph[i][j]
            elif j == i:
                sum_graph[i][j] = sum_graph[i - 1][j - 1] + graph[i][j]
            else:
                sum_graph[i][j] = max(
                    sum_graph[i - 1][j - 1],
                    sum_graph[i - 1][j]
                ) + graph[i][j]

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
sum_graph = [[0] * N for _ in range(N)]
dp()
print(max(sum_graph[N-1]))