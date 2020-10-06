import heapq

n = int(input())
q = list()
for _ in range(n):
    heapq.heappush(q, int((input())))

if n == 1:
    print(0)
    exit()

answer = 0
while len(q) > 1:
    val = heapq.heappop(q) + heapq.heappop(q)
    answer += val
    heapq.heappush(q, val)

print(answer)