graph = None


def add(key, x, y, add_or_sub):
    global graph

    for i in range(len(key)):
        for j in range(len(key)):
            graph[x + i][y + j] += add_or_sub * key[i][j]


def check(key, lock, x, y):
    add(key, x, y, 1)

    for i in range(len(lock)):
        for j in range(len(lock)):
            if graph[len(key) + i - 1][len(key) + j - 1] != 1:
                add(key, x, y, -1)
                return False
    return True


def rotate(key):  # 반시계 방향으로 회전
    size = len(key)
    arr = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            arr[size - j - 1][i] = key[i][j]
    return arr


def solution(key, lock):
    # 완전탐색을 위한 그래프 생성
    global graph
    graph = [[0] * (2 * len(key) + len(lock) - 2) for _ in range(2 * len(key) + len(lock) - 2)]
    for i in range(len(lock)):
        for j in range(len(lock)):
            graph[len(key) + i - 1][len(key) + j - 1] = lock[i][j]

    for _ in range(4):
        for i in range(len(graph) - len(key) + 1):
            for j in range(len(graph) - len(key) + 1):
                if check(key, lock, i, j):
                    return True
        key = rotate(key)

    return False