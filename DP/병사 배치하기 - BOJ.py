n = int(input())
arr = list(map(int, input().split()))

answer = [1] * n

for i in range(n):
    for a in range(len(arr[:i])):
        if arr[i] < arr[a] and answer[i] < answer[a] + 1:
            answer[i] = answer[a] + 1

print(n - max(answer))