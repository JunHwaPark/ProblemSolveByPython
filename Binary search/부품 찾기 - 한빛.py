n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()


def b_search(start, end, val):
    mid = (start + end) // 2
    if start > end:
        return False
    elif arr1[mid] == val:
        return True
    elif val < arr1[mid]:
        return b_search(start, mid - 1, val)
    elif arr1[mid] < val:
        return b_search(mid + 1, end, val)


for i in arr2:
    present = b_search(0, n - 1, i)
    if present:
        print('yes', end=' ')
    else:
        print('no', end=' ')
print()