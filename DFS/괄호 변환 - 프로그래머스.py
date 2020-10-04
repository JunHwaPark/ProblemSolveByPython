def is_correct(string):
    stack = list()
    for c in string:
        if c == '(':
            stack.append('(')
        elif len(stack) > 0:
            stack.pop()
        else:
            return False
    return True


def dfs(string):
    if len(string) == 0:  # 1번
        return ''

    c_open = 0
    c_close = 0

    for i in range(len(string)):
        if string[i] == '(':
            c_open += 1
        else:
            c_close += 1

        if c_open == c_close:  # 2번
            if is_correct(string[:i + 1]):  # 3번
                return string[:i + 1] + dfs(string[i + 1:])
            else:  # 4번
                v = '(' + dfs(string[i + 1:]) + ')'  # 4-1 ~ 4-3
                tmp = ''
                for a in range(1, i):  # 4-4
                    if string[a] == '(':
                        tmp += ')'
                    else:
                        tmp += '('
                return v + tmp


def solution(p):
    answer = dfs(p)
    return answer