import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
dist_from_1 = [INF] * 101
dist_from_K = [INF] * 101
route = [[] for _ in range(101)]
q = list()
for _ in range(m):
    a, b = map(int, input().split())
    route[a].append(b)
    route[b].append(a)
x, k = map(int, input().split())
heapq.heappush(q, (0, 1))
dist_from_1[1] = 0


def dijkstra(dist_from):
    while q:
        dist, now = heapq.heappop(q)
        if dist_from[now] < dist:
            continue
        for i in route[now]:
            if dist_from[i] > dist + 1:
                dist_from[i] = dist + 1
                heapq.heappush(q, (dist + 1, i))


dijkstra(dist_from_1)
heapq.heappush(q, (0, k))
dist_from_K[k] = 0
dijkstra(dist_from_K)
if dist_from_1[k] + dist_from_K[x] >= INF:
    print(-1)
else:
    print(dist_from_1[k] + dist_from_K[x])