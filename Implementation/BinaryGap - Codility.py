def solution(N):
    string = bin(N)[2:]
    answer = 0
    count = 0
    flag = False
    for s in string:
        if s == '0':
            count += 1
        else:
            if flag:
                if answer < count:
                    answer = count
                count = 0
            else:
                flag = True
    return answer