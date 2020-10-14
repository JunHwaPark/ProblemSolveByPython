n = int(input())

i2 = i3 = i5 = 0
m2, m3, m5 = 2, 3, 5

q = list()
q.append(1)
while len(q) < n:
    now = min(m2, m3, m5)
    q.append(now)
    if m2 == now:
        i2 += 1
        m2 = q[i2] * 2
    if m3 == now:
        i3 += 1
        m3 = q[i3] * 3
    if m5 == now:
        i5 += 1
        m5 = q[i5] * 5

print(q[n - 1])