n = int(input())
arr = list(map(int, input().split()))

maxarr = [0] * n

maxarr[0] = arr[0]
maxarr[1] = max(arr[0], arr[1])

for i in range(2, n):
    maxarr[i] = max(maxarr[i - 2] + arr[i], maxarr[i - 1])
print(maxarr[n - 1])