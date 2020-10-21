from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    visited = [False] * 10000
    a, b = map(int, input().split())

    q = deque()
    if a == b:
        print()
    else:
        q.append((a, ''))

    while q:
        val, history = q.popleft()

        # D
        d = (val * 2) % 10000
        if d == b:
            print(history + 'D')
            break
        elif not visited[d]:
            q.append((d, history + 'D'))
            visited[d] = True

        # S
        s = 0
        if val == 0:
            s = 9999
        else:
            s = val - 1
        if s == b:
            print(history + 'S')
            break
        elif not visited[s]:
            q.append((s, history + 'S'))
            visited[s] = True

        # L
        l = (val % 1000) * 10 + val // 1000
        if l == b:
            print(history + 'L')
            break
        elif not visited[l]:
            q.append((l, history + 'L'))
            visited[l] = True

        # R
        r = (val % 10) * 1000 + val // 10
        if r == b:
            print(history + 'R')
            break
        elif not visited[r]:
            q.append((r, history + 'R'))
            visited[r] = True