answer = 0


def b_search(start, end, n, arr):
    if start >= end:
        return
    global answer
    mid = (start + end) // 2
    count = 0
    for i in arr:
        count += mid // i

    if count >= n:
        answer = mid
        b_search(start, mid, n, arr)
    else:
        b_search(mid + 1, end, n, arr)


def solution(n, times):
    b_search(1, max(times) * n, n, times)
    return answer