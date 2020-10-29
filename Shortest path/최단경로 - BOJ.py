import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)
v, e = map(int, input().split())
start = int(input())
dist = [INF] * (v + 1)

route = dict()
for _ in range(e):
    u, d, w = map(int, input().split())
    if u not in route:
        route[u] = list()
    route[u].append((w, d))


dist[start] = 0
q = list()
heapq.heappush(q, (0, start))

while q:
    cost, now = heapq.heappop(q)
    if cost > dist[now]:
        continue
    if now not in route:
        continue
    for c, node in route[now]:
        if dist[node] > cost + c:
            dist[node] = cost + c
            heapq.heappush(q, (dist[node], node))

for i in range(1, v + 1):
    if dist[i] < INF:
        print(dist[i])
    else:
        print('INF')