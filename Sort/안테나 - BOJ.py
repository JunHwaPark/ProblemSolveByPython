n = int(input())
house = list(map(int, input().split()))
house.sort()
if n % 2 == 1:
    print(house[len(house) // 2])
else:
    val1 = house[len(house) // 2]
    val2 = house[len(house) // 2 - 1]
    print(min(val1, val2))