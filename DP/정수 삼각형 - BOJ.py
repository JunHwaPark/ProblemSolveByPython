n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = [list() for _ in range(n)]
index = 0
for i in arr[n - 1]:
    answer[0].append(i)

for a in arr[n - 2::-1]:
    index += 1
    for i in range(len(a)):
        answer[index].append(a[i] + max(answer[index - 1][i], answer[index - 1][i + 1]))

print(answer[-1][0])