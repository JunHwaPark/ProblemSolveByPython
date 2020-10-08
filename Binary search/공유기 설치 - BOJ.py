import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
answer = 0


def ok(val):
    count = 1
    now = arr[0]
    for a in arr[1:]:
        if a >= now + val:
            now = a
            count += 1
    if count >= c:
        return True
    return False


def binary_search(start, end):
    global answer
    if start > end:
        return
    mid = (start + end) // 2
    if ok(mid):
        answer = mid
        binary_search(mid + 1, end)
    else:
        binary_search(start, mid - 1)


binary_search(1, arr[n - 1] - arr[0])
print(answer)