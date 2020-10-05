from collections import deque


def solution(board):
    size = len(board)
    dd = ((-1, 0), (0, 1), (1, 0), (0, -1))
    visited = list()
    visited.append(((0, 0), (0, 1)))
    q = deque()
    q.append(((0, 0), (0, 1), 0))  # 좌표1, 좌표2, count

    answer = 0
    while q:
        now = q.popleft()
        answer = now[2]
        if now[0] == (size - 1, size - 1) or now[1] == (size - 1, size - 1):
            break
        # 상우하좌 이동
        for i in range(4):
            pos1 = (now[0][0] + dd[i][0], now[0][1] + dd[i][1])
            pos2 = (now[1][0] + dd[i][0], now[1][1] + dd[i][1])
            if 0 <= pos1[0] < size and 0 <= pos1[1] < size and 0 <= pos2[0] < size and 0 <= pos2[1] < size and \
                    board[pos1[0]][pos1[1]] == 0 and board[pos2[0]][pos2[1]] == 0 and (pos1, pos2) not in visited:
                q.append((pos1, pos2, now[2] + 1))
                visited.append((pos1, pos2))

        # 가로방향일 때
        if now[0][0] == now[1][0]:
            top = now[0][0] - 1
            bottom = now[0][0] + 1
            # 상단 2칸이 모두 비어있을 때
            if 0 <= top < size and board[top][now[0][1]] == 0 and board[top][now[1][1]] == 0:
                if ((top, now[0][1]), now[0]) not in visited:
                    q.append(((top, now[0][1]), now[0], now[2] + 1))
                    visited.append(((top, now[0][1]), now[0]))
                if ((top, now[1][1]), now[1]) not in visited:
                    q.append(((top, now[1][1]), now[1], now[2] + 1))
                    visited.append(((top, now[1][1]), now[1]))
            # 하단 2칸이 모두 비어있을 때
            if 0 <= bottom < size and board[bottom][now[0][1]] == 0 and board[bottom][now[1][1]] == 0:
                if (now[0], (bottom, now[0][1])) not in visited:
                    q.append((now[0], (bottom, now[0][1]), now[2] + 1))
                    visited.append((now[0], (bottom, now[0][1])))
                if (now[1], (bottom, now[1][1])) not in visited:
                    q.append((now[1], (bottom, now[1][1]), now[2] + 1))
                    visited.append((now[1], (bottom, now[1][1])))
        else:   # 세로방향일 때
            left = now[0][1] - 1
            right = now[0][1] + 1
            # 좌측 2칸이 모두 비어있을 때
            if 0 <= left < size and board[now[0][0]][left] == 0 and board[now[1][0]][left] == 0:
                if ((now[0][0], left), now[0]) not in visited:
                    q.append(((now[0][0], left), now[0], now[2] + 1))
                    visited.append(((now[0][0], left), now[0]))
                if ((now[1][0], left), now[1]) not in visited:
                    q.append(((now[1][0], left), now[1], now[2] + 1))
                    visited.append(((now[1][0], left), now[1]))
            # 우측 2칸이 모두 비어있을 때
            if 0 <= right < size and board[now[0][0]][right] == 0 and board[now[1][0]][right] == 0:
                if (now[0], (now[0][0], right)) not in visited:
                    q.append((now[0], (now[0][0], right), now[2] + 1))
                    visited.append((now[0], (now[0][0], right)))
                if (now[1], (now[1][0], right)) not in visited:
                    q.append((now[1], (now[1][0], right), now[2] + 1))
                    visited.append((now[1], (now[1][0], right)))
    return answer