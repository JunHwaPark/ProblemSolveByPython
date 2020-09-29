def solution(A, K):
    arr = list()
    for a in range(len(A)):
        arr.append(((a + K) % len(A), A[a]))
    arr.sort()
    answer = [c for i, c in arr]
    return answer