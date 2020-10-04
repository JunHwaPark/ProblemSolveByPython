# BFS로 풀이 가능. 2회차에는 BFS로 풀이!
# 현재 코드로는 PyPy3로만 통과하고, Python3로는 통과가 안됨.
# 추후 BFS로 작성하여 시간초과 나는지 확인 요망

import sys
sys.setrecursionlimit(10000)

dd = ((0, 1), (1, 0), (0, -1), (-1, 0))
n, l, r = map(int, input().split())
parent = [[[i, j] for j in range(n + 1)] for i in range(n + 1)]
graph = [[0] for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i] += map(int, input().split())


def find_parent(y, x):
    if parent[y][x] != [y, x]:
        parent[y][x] = find_parent(parent[y][x][0], parent[y][x][1])
    return parent[y][x]


def union(ay, ax, by, bx):
    ap, bp = find_parent(ay, ax), find_parent(by, bx)
    if ap[0] == bp[0]:
        if ap[1] < bp[1]:
            parent[bp[0]][bp[1]] = [ap[0], ap[1]]
        else:
            parent[ap[0]][ap[1]] = [bp[0], bp[1]]
    else:
        if ap[0] < bp[0]:
            parent[bp[0]][bp[1]] = [ap[0], ap[1]]
        else:
            parent[ap[0]][ap[1]] = [bp[0], bp[1]]


def dfs(y, x, arr, index):
    arr[index].append((y, x))
    for i in range(4):
        posy, posx = y + dd[i][0], x + dd[i][1]
        if 1 <= posy <= n and 1 <= posx <= n:
            ap, bp = find_parent(y, x), find_parent(posy, posx)
            if l <= abs(graph[y][x] - graph[posy][posx]) <= r and ap != bp:
                union(y, x, posy, posx)
                dfs(posy, posx, arr, index)


count = 0

while True:
    flag = False

    arr = list()
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if [i, j] == find_parent(i, j):
                arr.append(list())
                dfs(i, j, arr, len(arr) - 1)

    for u in arr:
        if len(u) > 1:
            summation = 0
            for a, b in u:
                summation += graph[a][b]
            val = summation // len(u)
            for a, b in u:
                graph[a][b] = val
            flag = True

    parent = [[[i, j] for j in range(n + 1)] for i in range(n + 1)]

    if not flag:
        break
    count += 1

print(count)