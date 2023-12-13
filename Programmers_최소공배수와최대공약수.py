### https://school.programmers.co.kr/learn/courses/30/lessons/12940

from math import gcd, lcm

def solution(n,m):
    return [gcd(n,m),lcm(n,m)]

### 함수 막아둠

def solution(n,m):
    gc_d, lc_m = 0,0
    for i in range(min(n,m),0,-1):
        if (n%i == 0) and (m%i == 0):
            gc_d += i
            break
    for i in range(max(n,m),(n*m+1)):
        if (i%n == 0) and (i%m == 0):
            lc_m += i
            break
    return [gc_d, lc_m]
