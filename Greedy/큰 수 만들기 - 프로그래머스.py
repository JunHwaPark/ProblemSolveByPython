from collections import deque

def solution(number, k):
    arr = [int(i) for i in number]
    stack = deque()
    strlen = len(number) - k
    for i in range(len(number)):
        if len(number) - (i + strlen) == 0:
            stack.append(arr[i])
            strlen -= 1
        elif len(stack) == 0:
            stack.append(arr[i])
            strlen -= 1
        else:
            while len(stack) > 0 and len(number) - (i + strlen) != 0:
                tmp = stack.pop()
                if tmp >= arr[i]:
                    stack.append(tmp)
                    break
                strlen += 1
            if strlen > 0:
                stack.append(arr[i])
                strlen -= 1
    answer = [str(i) for i in stack]
    return ''.join(answer)

# print(solution("123423123541", 3))