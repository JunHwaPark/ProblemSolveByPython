import heapq


def solution(food_times, k):
    q = list()
    size = len(food_times)
    for i in range(size):
        heapq.heappush(q, (food_times[i], i + 1))

    previous = 0
    while q:
        time, num = heapq.heappop(q)
        time_sum = size * (time - previous)

        if k >= time_sum:
            k -= time_sum
            previous = time
            size -= 1
        else:
            arr = [num]
            while q:
                t, n = heapq.heappop(q)
                arr.append(n)
            arr.sort()
            k %= size
            return arr[k]
    return -1