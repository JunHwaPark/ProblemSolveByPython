n = int(input())
arr = list(map(int, input().split()))


def binary_search(start, end):
    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    if start > end:
        return -1

    if mid > arr[mid]:
        return binary_search(mid + 1, end)
    else:
        return binary_search(start, mid - 1)


print(binary_search(0, n - 1))