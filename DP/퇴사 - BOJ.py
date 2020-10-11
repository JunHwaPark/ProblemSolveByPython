n = int(input())

answer = [list() for _ in range(n + 1)]
for ans in answer:
    ans.append(0)
    ans.append(list())

for i in range(n):
    day, money = map(int, input().split())
    if 0 < day + i <= n:
        answer[day + i][1].append([day, money])

for i in range(1, n + 1):
    if answer[i - 1][0] > answer[i][0]:
        answer[i][0] = answer[i - 1][0]
    for day, money in answer[i][1]:
        if answer[i][0] < answer[i - day][0] + money:
            answer[i][0] = answer[i - day][0] + money

print(answer[-1][0])