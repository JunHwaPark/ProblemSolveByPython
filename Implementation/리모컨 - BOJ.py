n = int(input())
m = int(input())
lost = list()

if m > 0:
    lost = list(map(int, input().split()))

if n == 100:
    print(0)
elif n > 100:
    minv = 100
    maxv = 100
    for i in range(n, 100, -1):
        s = str(i)
        flag = True
        for c in s:
            if int(c) in lost:
                flag = False
        if flag:
            minv = i
            break
    for i in range(n, 2 * n - minv):
        s = str(i)
        flag = True
        for c in s:
            if int(c) in lost:
                flag = False
        if flag:
            maxv = i
            break
    if maxv == 100:
        val = (minv, abs(n - minv))
    else:
        val = (maxv, abs(n - maxv))
    print(min(abs(100 - n), len(str(val[0])) + val[1]))
else:
    minv = 100
    maxv = 100
    for i in range(n, 100):
        s = str(i)
        flag = True
        for c in s:
            if int(c) in lost:
                flag = False
        if flag:
            maxv = i
            break
    for i in range(n, -1, -1):
        s = str(i)
        flag = True
        for c in s:
            if int(c) in lost:
                flag = False
        if flag:
            minv = i
            break
    if abs(n - minv) > abs(n - maxv):
        val = (maxv, abs(n - maxv))
    else:
        val = (minv, abs(n - minv))
    print(min(abs(100 - n), len(str(val[0])) + val[1]))