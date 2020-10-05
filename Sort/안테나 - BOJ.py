n = int(input())
house = list(map(int, input().split()))
house.sort()
if n % 2 == 1:
    print(house[len(house) // 2])
else:
    print(house[len(house) // 2 - 1])