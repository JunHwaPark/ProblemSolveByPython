n = int(input())
arr = [list() for _ in range(n)]
for a in arr:
    name, korean, english, math = input().split()
    korean = int(korean)
    english = int(english)
    math = int(math)
    a += [name, korean, english, math]
arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for a in arr:
    print(a[0])