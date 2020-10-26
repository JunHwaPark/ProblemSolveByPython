from itertools import combinations

n, m = map(int, input().split())
# for comb in combinations(range(1, n + 1), m):
#     for i in comb:
#         print(i, end=' ')
#     print()
#


def backtracking(comb, index, num):
    if len(comb) == num:
        for i in comb:
            print(i, end=' ')
        print()
    elif len(comb) > n:
        return

    for i in range(index, n + 1):
        backtracking(comb[:] + [i], i + 1, num)


backtracking(list(), 1, m)