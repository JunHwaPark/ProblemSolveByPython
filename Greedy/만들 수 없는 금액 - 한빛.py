n = int(input())
arr = list(map(int, input().split()))
arr.sort()
target = 1
for i in arr:
    if target < i:
        break
    else:
        target += i
print(target)