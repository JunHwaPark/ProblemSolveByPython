import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = graph[0][0]
for i in range(1, n):
    dp[i][0] = graph[i][0] + dp[i - 1][0]
    dp[0][i] = graph[0][i] + dp[0][i - 1]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = graph[i][j] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    dup = dp[x1 - 2][y1 - 2]
    if x1 - 2 >= 0:
        upper = dp[x1 - 2][y2 - 1]
    else:
        upper = 0
        dup = 0
    if y1 - 2 >= 0:
        left = dp[x2 - 1][y1 - 2]
    else:
        left = 0
        dup = 0
    print(dp[x2 - 1][y2 - 1] - upper - left + dup)