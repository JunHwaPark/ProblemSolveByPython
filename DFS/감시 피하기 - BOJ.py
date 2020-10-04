from itertools import combinations

dd = ((-1, 0), (0, 1), (1, 0), (0, -1))
n = int(input())
graph = [[' '] for _ in range(n + 1)]
empty = list()
teachers = list()
for i in range(1, n + 1):
    graph[i] += input().split()
    for j in range(1, n + 1):
        if graph[i][j] == 'X':
            empty.append((i, j))
        elif graph[i][j] == 'T':
            teachers.append((i, j))

for obj in combinations(empty, 3):
    for y, x in obj:
        graph[y][x] = 'O'

    flag = False
    for teacher in teachers:
        for i in range(4):
            y, x = teacher
            while 1 <= y <= n and 1 <= x <= n and graph[y][x] != 'O':
                if graph[y][x] == 'S':
                    flag = True
                    break
                y += dd[i][0]
                x += dd[i][1]
            if flag:
                break
        if flag:
            break

    if not flag:
        print('YES')
        exit()

    for y, x in obj:
        graph[y][x] = 'X'

print('NO')