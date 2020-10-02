from copy import deepcopy
from itertools import permutations

length = 0


def fix(weak, dist, point):
    index = 0
    size = len(weak)

    for d in dist:
        val = weak[index] + d
        for a in range(index, size):
            if weak[a] <= val:
                index = a + 1
            else:
                break
        if index == size:
            return True

    return False


def check(weak, dist):
    size = len(weak)
    for i in range(size):
        tmp = [weak[a] + length for a in range(i)]
        if fix(weak[i:] + tmp, dist, i):
            return True
    return False


def solution(n, weak, dist):
    global length
    length = n
    dist.sort(reverse=True)

    for i in range(1, len(dist) + 1):
        perms = permutations(dist, i)
        for perm in perms:
            if check(weak, perm):
                return i

    return -1