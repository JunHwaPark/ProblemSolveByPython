n = input()
if sum([int(c) for c in n[:len(n) // 2]]) == sum([int(c) for c in n[len(n) // 2:]]):
    print('LUCKY')
else:
    print('READY')