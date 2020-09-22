n, m = map(int, input().split())
parent = [i for i in range(n + 1)]


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
    c, a, b = map(int, input().split())
    if c == 0:
        union(a, b)
    else:
        ap, bp = find_parent(a), find_parent(b)
        if ap == bp:
            print("YES")
        else:
            print("NO")