### https://school.programmers.co.kr/learn/courses/30/lessons/12948

def solution(n):
    n = list(n)
    n[:-4] = ['*']*len(n[:-4])
    n=''.join(n)
    return n
    

# 문자열 곱셈을 이용한 풀이가 더 깔끔
def solution(n):
    return '*'*(len(n)-4) + n[-4:]
