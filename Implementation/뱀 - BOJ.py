from collections import deque


go_dir = ((0, 1), (1, 0), (0, -1), (-1, 0))
dir = 0
time = 0
snake = deque()
snake.append((1, 1))
n = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]

k = int(input())
for _ in range(k):
    y, x = map(int, input().split())
    graph[y][x] = 2


def go():
    global time
    time += 1
    head = snake.pop()
    snake.append(head)
    y, x = head[0] + go_dir[dir][0], head[1] + go_dir[dir][1]

    if not 1 <= y <= n or not 1 <= x <= n or (y, x) in snake:
        print(time)
        exit()
    elif graph[y][x] == 2:
        snake.append((y, x))
        graph[y][x] = 0
    else:
        snake.append((y, x))
        snake.popleft()


l = int(input())
for _ in range(l):
    a, c = input().split()
    a = int(a)
    repeat = a - time
    for _ in range(repeat):
        go()

    if c == 'L':
        dir = (dir + 3) % 4
    else:
        dir = (dir + 1) % 4

while True:
    go()