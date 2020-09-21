x = int(input())

arr = [0] * (x + 1)

for i in range(1, x + 1):
    count = arr[i]
    if i * 5 <= x and (arr[i * 5] == 0 or arr[i * 5] > count + 1):
        arr[i * 5] = count + 1
    if i * 3 <= x and (arr[i * 3] == 0 or arr[i * 3] > count + 1):
        arr[i * 3] = count + 1
    if i * 2 <= x and (arr[i * 2] == 0 or arr[i * 2] > count + 1):
        arr[i * 2] = count + 1
    if i + 1 <= x and (arr[i + 1] == 0 or arr[i + 1] > count + 1):
        arr[i + 1] = count + 1
print(arr[x])