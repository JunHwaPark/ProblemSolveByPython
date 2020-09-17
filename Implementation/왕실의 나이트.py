inputpos = input()
x, y = int(inputpos[1]), ord(inputpos[0]) - ord('a') + 1
count = 0
if x - 2 >= 1:
    if y - 1 >= 1: count += 1
    if y + 1 <= 8: count += 1
if x + 2 <= 8:
    if y - 1 >= 1: count += 1
    if y + 1 <= 8: count += 1
if y - 2 >= 1:
    if x - 1 >= 1: count += 1
    if x + 1 <= 8: count += 1
if y + 2 <= 8:
    if x - 1 >= 1: count += 1
    if x + 1 <= 8: count += 1
print(count)

# dx, dy 이용
steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

count = 0
for step in steps:
    row = x + step[0]
    column = y + step[1]
    if 1 <= row <= 8 and 1 <= column <= 8:
        count += 1
print(count)