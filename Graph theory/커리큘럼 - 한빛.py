# 위상 정렬
from collections import deque
queue = deque()
n = int(input())
lectures = [[[]] for _ in range(n + 1)]
for i in range(1, n + 1):
    info = list(map(int, input().split()))
    for j in info[1:-1]:
        lectures[j][0].append(i)    # 이어지는 강의 리스트
    lectures[i].append(info[0])     # 해당과목 소요시간
    lectures[i].append(info[0])     # 해당과목 소요시간(선수과목 포함)
    lectures[i].append(len(info) - 2)   # 선수과목 갯수
    if lectures[i][3] == 0:         # 선수과목 없으면 큐에 추가
        queue.append(i)

while queue:    # 큐가 빌 때까지 계속 반복
    now = queue.popleft()
    for lecture in lectures[now][0]:
        lectures[lecture][2] = max(lectures[lecture][2], lectures[lecture][1] + lectures[now][2])
        lectures[lecture][3] -= 1
        if lectures[lecture][3] == 0:
            queue.append(lecture)

for lecture in lectures[1:]:
    print(lecture[2])