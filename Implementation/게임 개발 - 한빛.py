def rotate(d):
    d -= 1
    if d < 0:
        d = 3
    return d


n, m = map(int, input().split())
a, b, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr[a][b] = 3

dd = ((-1, 0), (0, 1), (1, 0), (0, -1))
rotate_count = 0
visit_count = 1
while True:
    d = rotate(d)
    # 맵 바깥으로 나가는지 확인
    if not 0 <= a + dd[d][0] <= n and not 0 <= b + dd[d][1] <= m:
        rotate_count += 1
    # 왼쪽이 바다가 아닌 안가본 곳일 때
    elif arr[a + dd[d][0]][b + dd[d][1]] == 0:
        a += dd[d][0]
        b += dd[d][1]
        arr[a][b] = 3
        visit_count += 1
        rotate_count = 0
    # 나머지 = 왼쪽이 가본 곳이거나 바다일 때
    else:
        rotate_count += 1
    # 4번 회전했을 때 == 사방이 바다이거나 가본 곳일 때
    if rotate_count == 4:
        a -= dd[d][0]
        b -= dd[d][1]
        if (not 0 <= a <= n and not 0 <= b <= m) or arr[a][b] != 0:
            break
        visit_count += 1
print(visit_count)