from _collections import deque

n, m = map(int, input().split())
maze = list()
maze.append(list())
for _ in range(n):
    maze.append([0] + list(map(int, input())))
dd = ((-1, 0, 1), (0, 1, 1), (1, 0, 1), (0, -1, 1))


def cango(pos):
    if not 1 <= pos[0] <= n or not 1 <= pos[1] <= m:
        return False
    elif maze[pos[0]][pos[1]] != 1:
        return False
    return True


queue = deque()
queue.append((1, 1, 1))
while queue:
    pos = queue.popleft()
    maze[pos[0]][pos[1]] = pos[2]
    if pos[0] == n and pos[1] == m:
        break
    for i in range(4):
        tmpy = pos[0] + dd[i][0]
        tmpx = pos[1] + dd[i][1]
        if cango((tmpy, tmpx)):
            queue.append((tmpy, tmpx, pos[2] + 1))
print(maze[n][m])