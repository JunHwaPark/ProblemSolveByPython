a, b, c = map(int, input().split())

answer = 1
mul = a % c
while b > 0:
    if b % 2 == 1:
        answer *= mul
        answer %= c
    mul = ((mul % c) ** 2) % c
    b //= 2
print(answer)