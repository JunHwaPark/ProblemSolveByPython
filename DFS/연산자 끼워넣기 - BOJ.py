from copy import deepcopy

n = int(input())
arr = list(map(int, input().split()))
operators = list(map(int, input().split()))
answer = [-int(1e9), int(1e9)]


def dfs(operand, used, index):
    if index == n:
        if operand > answer[0]:
            answer[0] = operand
        if operand < answer[1]:
            answer[1] = operand
        return

    for i in range(4):
        if used[i] < operators[i]:
            tmp_used = deepcopy(used)
            tmp_used[i] += 1
            if i == 0:
                dfs(operand + arr[index], tmp_used, index + 1)
            elif i == 1:
                dfs(operand - arr[index], tmp_used, index + 1)
            elif i == 2:
                dfs(operand * arr[index], tmp_used, index + 1)
            else:
                num = abs(operand) // arr[index]
                if operand < 0:
                    num *= -1
                dfs(num, tmp_used, index + 1)


dfs(arr[0], [0, 0, 0, 0], 1)
print(answer[0])
print(answer[1])