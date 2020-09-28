def solution(brown, yellow):
    size = brown + yellow
    answer = []
    for i in range(3, size // 2 + 1):
        if size % i == 0 and (size // i - 2) * (i - 2) == yellow:
            answer.append(size // i)
            answer.append(i)
            break
    return answer
