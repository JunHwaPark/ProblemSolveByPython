numbers = input()
arr = [int(i) for i in numbers]
result = arr[0]
for i in arr[1:]:
    result = max(result + i, result * i)
print(result)