n, m = map(int, input().split())
arr = list(map(int, input().split()))
val = [0] * (n + 1)
for i in arr:
    val[i] += 1
count = 0
for i in range(1, m + 1):
    count += val[i] * (sum(val[i + 1:]))
print(count)