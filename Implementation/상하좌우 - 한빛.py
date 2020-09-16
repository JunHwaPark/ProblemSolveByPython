n = int(input())
move = input().split()
pos = [1, 1]

for c in move:
    if c == 'L' and 1 < pos[1]:
        pos[1] -= 1
    elif c == 'R' and pos[1] < n:
        pos[1] += 1
    elif c == 'U' and 1 < pos[0]:
        pos[0] -= 1
    elif c == 'D' and pos[0] < n:
        pos[0] += 1
print(pos[0], pos[1])