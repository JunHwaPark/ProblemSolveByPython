from collections import deque

n = int(input())
arr = [list() for _ in range(n + 1)]
answer = [-1] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

q = deque()
q.append(1)

while q:
    now = q.popleft()
    for node in arr[now]:
        if answer[now] != node:
            answer[node] = now
            q.append(node)

for ans in answer[2:]:
    print(ans)