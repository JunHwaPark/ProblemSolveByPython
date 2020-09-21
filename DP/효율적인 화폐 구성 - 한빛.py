n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
value = [0] * 10001

for i in arr:
    value[i] = 1

for i in range(1, m + 1):
    if value[i] == 0:
        continue
    for j in range(n):
        if i + arr[j] > m:
            continue
        elif value[i + arr[j]] == 0:
            value[i + arr[j]] = value[i] + 1
        else:
            value[i + arr[j]] = min(value[i] + 1, value[i + arr[j]])
if value[m] == 0:
    print(-1)
else:
    print(value[m])