from itertools import combinations

n, m = map(int, input().split())
graph = [[0] for _ in range(n + 1)]
homes = list()
stores = list()

for i in range(1, n + 1):
    graph[i] += list(map(int, input().split()))
    for j in range(1, n + 1):
        if graph[i][j] == 1:
            homes.append((i, j))
        elif graph[i][j] == 2:
            stores.append((i, j))

answer = int(1e9)
combs = combinations(stores, m)

for comb in combs:
    town_chicken = 0
    for home in homes:
        chicken = int(1e9)
        for store in comb:
            dist = abs(home[0] - store[0]) + abs(home[1] - store[1])
            if chicken > dist:
                chicken = dist
        town_chicken += chicken
    if answer > town_chicken:
        answer = town_chicken
print(answer)