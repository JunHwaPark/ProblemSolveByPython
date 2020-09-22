import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
edges = list()


def find_parent(c):
    if parent[c] != c:
        parent[c] = find_parent(parent[c])
    return parent[c]


def union(a, b):
    ap, bp = find_parent(a), find_parent(b)
    if ap < bp:
        parent[bp] = ap
    else:
        parent[ap] = bp


for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

cost = 0
for edge in edges:
    c, a, b = edge
    if find_parent(a) != find_parent(b):
        last = c
        cost += c
        union(a, b)
print(cost - last)