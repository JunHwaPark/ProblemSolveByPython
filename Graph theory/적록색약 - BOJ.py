from collections import deque

dd = ((0, 1), (1, 0), (-1, 0), (0, -1))
n = int(input())
graph = [[c for c in input()] for _ in range(n)]
visited = [[False] * n for _ in range(n)]
answer = [0, 0]
q = deque()

# 일반인
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            color = graph[i][j]
            answer[0] += 1
            q.append((i, j))
            visited[i][j] = True
            while q:
                y, x = q.popleft()
                for d in range(4):
                    dy, dx = y + dd[d][0], x + dd[d][1]
                    if 0 <= dy < n and 0 <= dx < n and not visited[dy][dx] and color == graph[dy][dx]:
                        visited[dy][dx] = True
                        q.append((dy, dx))
# 적록색약
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            color = graph[i][j]
            answer[1] += 1
            q.append((i, j))
            visited[i][j] = True
            while q:
                y, x = q.popleft()
                for d in range(4):
                    dy, dx = y + dd[d][0], x + dd[d][1]
                    if 0 <= dy < n and 0 <= dx < n and not visited[dy][dx]:
                        if color == 'B' and color == graph[dy][dx]:
                            visited[dy][dx] = True
                            q.append((dy, dx))
                        elif color != 'B' and graph[dy][dx] != 'B':
                            visited[dy][dx] = True
                            q.append((dy, dx))
print(answer[0], answer[1])