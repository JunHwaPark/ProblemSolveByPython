def solution(N, stages):
    arr = [[] for _ in range(N + 1)]
    stages.sort(reverse=True)
    stage = N + 1
    count = stages.count(N + 1)
    index = count
    for i in range(N):
        stage -= 1
        while 0 <= index < len(stages) and stages[index] == stage:
            index += 1
        if index >0:
            arr[stage] = [(index - count) / index, stage]
        else:
            arr[stage] = [0, stage]
        count = index
    arr = sorted(arr[1:], key=lambda x: (-x[0], x[1]))
    answer = [arr[i][1] for i in range(N)]
    print(answer)
    return answer