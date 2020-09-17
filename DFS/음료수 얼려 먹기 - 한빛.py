n, m = map(int, input().split())
# tmp = [input() for _ in range(n)]
# arr = list()
# for s in tmp:
#     ints = list()
#     for i in s:
#         ints.append(int(i))
#     arr.append(ints)
arr = list()
for _ in range(n):
    arr.append(list(map(int, input())))
visited = [[False for _ in range(m)] for _ in range(n)]
dd = ((-1, 0), (0, 1), (1, 0), (0, -1))
count = 0


def dfs(y, x):
    # print(y, x)
    global visited
    visited[y][x] = True
    for i in range(4):
        tmpy = y + dd[i][0]
        tmpx = x + dd[i][1]
        if 0 <= tmpy < n and 0 <= tmpx < m and arr[tmpy][tmpx] == 0 and not visited[tmpy][tmpx]:
            dfs(tmpy, tmpx)


for a in range(n):
    for b in range(m):
        if not visited[a][b] and arr[a][b] == 0:
            dfs(a, b)
            count += 1
print(count)