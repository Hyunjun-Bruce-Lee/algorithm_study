### https://school.programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    if n%2 == 0:
        return '수박'*(int(n/2))
    else:
        return ('수박'*(n//2 + 1))[:n]

### 아래처럼 몫 나머지 이용하는게 연산 더 적음

def water_melon(n):
    return "수박" * (n//2) + "수" * (n%2)