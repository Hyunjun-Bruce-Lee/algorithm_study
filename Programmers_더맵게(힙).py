# https://programmers.co.kr/learn/courses/30/lessons/42626


scoville = [1, 2, 3, 9, 10, 12]
k = 50

def solution(scoville, k):
    answer = 0
    while min(scoville) <= k:
        answer += 1
        scoville.sort(reverse=True)
        first = scoville.pop()
        second = scoville.pop()
        value = first + (second * 2)
        print(value)
        scoville.append(value)
        if (len(scoville) == 1)&(scoville[0] < k):
            return -1
            break
    return answer

##### 위 코드 시간초과 아래로 바꿈 #####

import heapq

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] <= k:
        answer += 1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        value = first + (second * 2)
        heapq.heappush(scoville, value)
        if (len(scoville) == 1)&(scoville[0] < k):
            return -1
    return answer
