INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0
for _ in range(m):
    low, great = map(int, input().split())
    graph[low][great] = 1

for i in range(1, n + 1):
    for a in range(1, n + 1):
        if a == i:
            continue
        for b in range(1, n + 1):
            if b == i:
                continue
            if graph[a][b] > graph[a][i] + graph[i][b]:
                graph[a][b] = 1

answer = 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        answer += 1

print(answer)