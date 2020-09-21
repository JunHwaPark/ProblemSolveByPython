n = int(input())
arr = [0] * 1001
arr[0] = 1
arr[1] = 1

for i in range(2, n + 1):
    arr[i] = arr[i - 1] + 2 * arr[i - 2]
    arr[i] %= 796796
print(arr[n])