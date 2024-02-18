### https://school.programmers.co.kr/learn/courses/30/lessons/12921

def prime_num(num):
    for i in range(2,int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n):
    ans = 0
    for i in range(1,n+1):
        if prime_num(i):
            ans += 1
    return ans -1


### 아래는 에라토스너스의 체를 이용한 풀이라고함

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)