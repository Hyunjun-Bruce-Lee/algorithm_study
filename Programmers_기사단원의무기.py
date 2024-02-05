### https://school.programmers.co.kr/learn/courses/30/lessons/136798

def count_d(n):
    cnt = 0
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            cnt += 1
            if ( (i**2) != n) : 
                cnt += 1
    return cnt

def solution(number, limit, power):
    ans = 0
    for i in range(1,number +1):
        temp = count_d(i)
        if temp > limit:
            temp = power
        ans += temp
    return ans



