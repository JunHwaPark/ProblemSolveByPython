n = int(input())
arr = list()
for _ in range(n):
    data = input().split()
    arr.append((data[0], int(data[1])))

arr.sort(key=lambda x: x[1])
for student in arr:
    print(student[0], end=' ')
print()