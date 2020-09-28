def solution(numbers):
    answer = 0
    arr = [True] * int(10 ** len((numbers)))
    size = len(arr)
    for i in range(2, size):
        if arr[i]:
            # search
            nums = [c for c in numbers]
            isPrime = True
            for k in str(i):
                flag = False
                for a in range(len(nums)):
                    if nums[a] == k:
                        flag = True
                        nums[a] = '10'
                        break
                if not flag:
                    isPrime = False
                    break
            if isPrime:
                answer += 1
            for j in range(i * 2, size, i):
                arr[j] = False
    return answer