n, m = map(int, input().split())
arr = list(map(int, input().split()))
maximum = 0


def b_search(start, end, val):
    global maximum
    mid = (start + end) // 2
    length = 0
    for i in arr:
        if i > mid:
            length += i - mid
    if start > end:
        return None
    elif val <= length and maximum < mid:
        maximum = mid
        b_search(mid + 1, end, val)
    elif length < val:
        b_search(start, mid - 1, val)


b_search(0, max(arr), m)
print(maximum)