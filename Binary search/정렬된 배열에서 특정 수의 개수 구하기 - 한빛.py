n, x = map(int, input().split())
arr = list(map(int, input().split()))
s, e = n - 1, 0


def binary_search(start, end, val):
    global s, e
    if start > end:
        return

    mid = (start + end) // 2
    if arr[mid] == val:
        binary_search(start, mid - 1, val)
        binary_search(mid + 1, end, val)
    elif arr[mid] > val:
        e = mid
        binary_search(start, mid - 1, val)
    elif arr[mid] < val:
        s = mid
        binary_search(mid + 1, end, val)


binary_search(0, n - 1, x)
answer = e - s - 1
if answer > 0:
    print(answer)
else:
    print(-1)