graph = None


def is_possible(x, y):
    if graph[x][y] == 1:  # 기둥
        # 바닥이거나 // 보의 오른쪽 끝 부분 위에 있거나(왼쪽 끝에 있으면 같은 위치이므로 3) // 다른 기둥 위거나
        if y == 0 or (x > 0 and graph[x - 1][y] >= 2) or graph[x][y - 1] in (1, 3):
            return True
        else:
            return False
    elif graph[x][y] == 2:  # 보
        # 한쪽 끝 부분이 기둥 위에 있거나 // 양쪽 끝 부분이 다른 보와 동시에 연결
        if graph[x][y - 1] in (1, 3) or graph[x + 1][y - 1] in (1, 3) \
                or (x > 0 and graph[x - 1][y] >= 2 and graph[x + 1][y] >= 2):
            return True
        else:
            return False
    else:  # 기둥과 보 함께 설치
        # 다른 기둥 위거나 // 양쪽 끝 부분이 다른 보와 동시에 연결되거나 // 오른쪽 기둥 위거나
        if graph[x][y - 1] in (1, 3) or (x > 0 and graph[x - 1][y] >= 2 and graph[x + 1][y] >= 2) \
                or graph[x + 1][y - 1] in (1, 3):
            return True
        else:
            return False


def solution(n, build_frame):
    global graph
    graph = [[0] * (n + 1) for _ in range(n + 1)]

    for frame in build_frame:
        x, y, a, b = frame
        now = graph[x][y]
        a += 1

        if b == 0:
            graph[x][y] -= a
        else:
            graph[x][y] += a

        for i in range(n + 1):
            flag = False
            for j in range(n + 1):
                if graph[i][j] != 0 and not is_possible(i, j):
                    flag = True
                    graph[x][y] = now
                    break
            if flag:
                break

    answer = list()
    for i in range(n + 1):
        for j in range(n + 1):
            if graph[i][j] == 1:
                answer.append([i, j, 0])
            elif graph[i][j] == 2:
                answer.append([i, j, 1])
            elif graph[i][j] == 3:
                answer.append([i, j, 0])
                answer.append([i, j, 1])
    return answer