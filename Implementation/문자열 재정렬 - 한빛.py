string = input()
arr = list()
num = 0
for c in string:
    if c.isnumeric():
        num += int(c)
    elif c.isalpha():
        arr.append(c)
arr.sort()
print(''.join(arr) + str(num))