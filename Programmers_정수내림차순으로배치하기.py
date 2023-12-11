### https://school.programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    temp = sorted([int(i) for i in list(str(n))], reverse=True)
    return int(''.join(list(map(str,temp))))
