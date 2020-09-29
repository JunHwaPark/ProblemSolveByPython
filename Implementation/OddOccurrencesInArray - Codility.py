def solution(A):
    set1 = set()
    for i in A:
        if i in set1:
            set1.remove(i)
        else:
            set1.add(i)
    return list(set1)[0]