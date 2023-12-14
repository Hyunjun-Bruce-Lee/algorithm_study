### https://school.programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    temp_arr = list()
    for i in range(1,n+1):
        if n%i ==0:
            temp_arr.append(i)
    return sum(temp_arr)


### 모범답안, 시간 감소

def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])