shapes = (((0, 0), (1, 0), (2, 0), ((3, 0), (0, -1), (0, 1), (1, -1), (1, 1), (2, -1), (2, 1))),
          ((0, 0), (0, 1), (0, 2), ((0, 3), (-1, 0), (1, 0), (-1, 1), (1, 1), (-1, 2), (1, 2))),
          ((0, 0), (0, 1), (1, 0), (1, 1)),
          ((0, 0), (1, 0), (1, 1), (2, 1)),
          ((0, 1), (1, 0), (1, 1), (2, 0)),
          ((0, 0), (0, 1), (1, 1), (1, 2)),
          ((1, 0), (0, 1), (1, 1), (0, 2)))

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

answer = 0


def get_sum(y, x, li):
    summation = 0
    for l in li:
        summation += graph[y + l[0]][x + l[1]]
    return summation


for i in range(n):
    for j in range(m):
        for a in range(2):
            for b in range(7):
                try:
                    val = get_sum(i, j, shapes[a][:3] + shapes[a][3][b:b + 1])
                    if answer < val:
                        answer = val
                except IndexError:
                    pass
        for a in range(2, 7):
            try:
                val = get_sum(i, j, shapes[a])
                if answer < val:
                    answer = val
            except IndexError:
                pass
print(answer)