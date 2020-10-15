INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

for i in range(1, n + 1):
    for a in range(1, n + 1):
        if a == i:
            continue
        for b in range(1, n + 1):
            if b == i:
                continue
            if graph[a][b] > graph[a][i] + graph[i][b]:
                graph[a][b] = graph[a][i] + graph[i][b]

for g in graph[1:]:
    for town in g[1:]:
        if town < INF:
            print(town, end=' ')
        else:
            print(0, end=' ')
    print()