### https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    strings = [list(t)[i:i+len(p)] for i in range(0,len(t)-(len(p)-1))]
    cnt = 0
    for part in strings:
        if int(''.join(part)) <= int(p):
            cnt += 1
    return cnt
