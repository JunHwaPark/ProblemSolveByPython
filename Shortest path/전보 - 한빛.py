import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
min_dist = [INF] * (n + 1)
min_dist[c] = 0


def dijkstra():
    q = list()
    heapq.heappush(q, (0, c))
    while q:
        dist, now = heapq.heappop(q)
        if min_dist[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if min_dist[i[0]] > cost:
                min_dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra()
count = 0
time = 0
for i in min_dist[1:]:
    if i == 0:
        continue
    if i < INF:
        count += 1
        time = max(time, i)
print(count, time)