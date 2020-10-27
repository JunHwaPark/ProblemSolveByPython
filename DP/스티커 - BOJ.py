t = int(input())
for _ in range(t):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(2)]
    answer = [[0] * n for _ in range(2)]
    answer[0][0], answer[1][0] = graph[0][0], graph[1][0]
    ans = max(answer[0][0], answer[1][0])

    for i in range(1, n):
        for j in range(2):
            if i >= 2:
                answer[j][i] = graph[j][i] + max(answer[(j + 1) % 2][i - 1], answer[0][i - 2], answer[1][i - 2])
            else:
                answer[j][i] = graph[j][i] + answer[(j + 1) % 2][i - 1]
            ans = max(ans, answer[j][i])
    print(ans)