s = input()
val = s[0]
count = 0
for c in s:
    if val != c:
        val = c
        count += 1
if count % 2 == 0:
    print(count // 2)
else:
    print(count // 2 + 1)