def solution(s):
    if len(s) == 1:
        return 1
    answer = 1000
    for i in range(1, len(s) // 2 + 1):
        index = 0
        count = 0
        length = 0
        cmp = s[:i]
        for j in range(0, len(s) - i + 1, i):
            if s[j:].startswith(cmp):
                count += 1
            else:
                if count > 1:
                    length += (len(str(count)) + i)
                else:
                    length += i
                cmp = s[j:j + i]
                count = 1

        if count > 1:
            length += len(str(count)) + i
        else:
            length += i

        if len(s) % i > 0:
            length += len(s) % i

        if length < answer:
            answer = length
    return answer