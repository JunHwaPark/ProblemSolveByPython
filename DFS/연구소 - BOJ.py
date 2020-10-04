from itertools import combinations
from copy import deepcopy

dd = ((0, 1), (1, 0), (0, -1), (-1, 0))
n, m = map(int, input().split())
graph = list()
empty = list()
virus = list()
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 2:
            virus.append([i, j])
        elif tmp[j] == 0:
            empty.append([i, j])
    graph.append(tmp)


def dfs(graph, y, x):
    graph[y][x] = 2
    for i in range(4):
        posy = y + dd[i][0]
        posx = x + dd[i][1]
        if 0 <= posy < n and 0 <= posx < m and graph[posy][posx] == 0:
            dfs(graph, posy, posx)


answer = 0
for comb in combinations(empty, 3):
    tmp_graph = deepcopy(graph)
    for y, x in comb:
        tmp_graph[y][x] = 1
    count = 0
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                dfs(tmp_graph, i, j)
    for g in tmp_graph:
        count += g.count(0)
    if answer < count:
        answer = count
print(answer)