# 구현, bfs 혼합문제
from collections import deque

dd = ((0, 1), (1, 0), (-1, 0), (0, -1))
size = 2
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
now = None

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            now = (i, j, 0)
            graph[i][j] = 0

need_to_size_up = 2
t = 0

while True:
    can_eat = list()
    q = deque()
    q.append(now)
    visited = [[False] * n for _ in range(n)]
    visited[now[0]][now[1]] = True
    flag = False
    while q:
        y, x, time = q.popleft()
        if 0 < graph[y][x] < size:
            flag = True
            can_eat.append((y, x, time))
            t = time
        for i in range(4):
            if flag:
                break
            dy, dx = y + dd[i][0], x + dd[i][1]
            if 0 <= dy < n and 0 <= dx < n and graph[dy][dx] <= size and not visited[dy][dx]:
                visited[dy][dx] = True
                q.append((dy, dx, time + 1))
    if len(can_eat) == 0:
        print(t)
        exit()
    else:
        can_eat.sort(key=lambda z: (z[2], z[0], z[1]))
        now = can_eat[0]
        if need_to_size_up == 1:
            size += 1
            need_to_size_up = size
        else:
            need_to_size_up -= 1
        graph[now[0]][now[1]] = 0