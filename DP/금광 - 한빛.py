t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [list() for _ in range(n)]

    if n == 1:
        print(sum(arr[0]))
        continue

    answer = [list() for _ in range(m)]
    value = list(map(int, input().split()))
    index = 0
    for row in range(n):
        for column in range(m):
            arr[row].append(value[index])
            index += 1

    for i in range(n):
        answer[0].append(arr[i][0])

    for i in range(1, m):
        for j in range(n):
            if j == 0:
                answer[i].append(arr[j][i] + max(answer[i - 1][0], answer[i - 1][1]))
            elif j == n - 1:
                answer[i].append(arr[j][i] + max(answer[i - 1][n - 1], answer[i - 1][n - 2]))
            else:
                answer[i].append(arr[j][i] + max(answer[i - 1][j - 1], answer[i - 1][j], answer[i - 1][j + 1]))

    print(max(answer[m - 1]))