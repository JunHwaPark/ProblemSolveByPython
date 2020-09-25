def solution(numbers):
    arr = list(map(str, numbers))
    answer = ''.join(sorted(arr, key = lambda x: x * 5, reverse = True))
    return str(int(answer))
