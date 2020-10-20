n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for a in range(n):
        if a == i:
            continue
        for b in range(n):
            if b == i:
                continue
            if graph[a][b] == 0 and graph[a][i] + graph[i][b] == 2:
                graph[a][b] = 1

for g in graph:
    for a in g:
        print(a, end=' ')
    print()