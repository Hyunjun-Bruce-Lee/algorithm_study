### https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(t):
    t = sorted([int(i) for i in t.split(' ')])
    return f'{t[0]} {t[-1]}'