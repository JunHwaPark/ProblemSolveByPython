def solution(citations):
    answer = 0
    arr = [0]
    arr += sorted(citations, reverse = True)
    for i in range(1, len(arr)):
        if i <= arr[i]:
            answer = i
        else:
            break
    return answer