# 이분탐색으로 해결. 추후 Trie 자료구조로 요망
from bisect import bisect_left, bisect_right


def solution(words, queries):
    answer = list()
    forward = [list() for _ in range(10001)]
    backward = [list() for _ in range(10001)]

    for word in words:
        forward[len(word)].append(word)
        backward[len(word)].append(word[::-1])
    for i in range(10001):
        forward[i].sort()
        backward[i].sort()

    for query in queries:
        if query[0] != '?':
            l = bisect_left(forward[len(query)], query.replace('?', 'a'))
            r = bisect_right(forward[len(query)], query.replace('?', 'z'))
            answer.append(r - l)
        else:
            l = bisect_left(backward[len(query)], query[::-1].replace('?', 'a'))
            r = bisect_right(backward[len(query)], query[::-1].replace('?', 'z'))
            answer.append(r - l)
    return answer