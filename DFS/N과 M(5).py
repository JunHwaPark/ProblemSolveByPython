from itertools import permutations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

# for perm in permutations(arr, m):
#     for i in perm:
#         print(i, end=' ')
#     print()


def backtracking(li):
    if len(li) == m:
        for i in li:
            print(i, end=' ')
        print()
    elif len(li) > len(arr):
        return

    for i in range(0, n):
        if arr[i] not in li:
            backtracking(li + [arr[i]])


backtracking(list())