from collections import deque

dd = ((-1, 0), (0, 1), (1, 0), (0, -1))
n, k = map(int, input().split())
q = deque()
viruses = list()
graph = [[0] for _ in range(n + 1)]
for i in range(1, n + 1):
    arr = list(map(int, input().split()))
    graph[i] += arr
    for j in range(1, n + 1):
        if graph[i][j] != 0:
            viruses.append((graph[i][j], 0, i, j))

s, x, y = map(int, input().split())
viruses.sort()
for virus in viruses:
    q.append(virus)

while q:
    virus = q.popleft()

    for i in range(4):
        posx, posy = virus[2] + dd[i][0], virus[3] + dd[i][1]
        if 1 <= posx <= n and 1 <= posy <= n and graph[posx][posy] == 0 and virus[1] < s:
            graph[posx][posy] = virus[0]
            q.append((virus[0], virus[1] + 1, posx, posy))

print(graph[x][y])