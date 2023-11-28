### https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    re_string = str()
    while True:
        q,r = divmod(n,3)
        re_string += str(r)
        if q == 0:
            break
        n = q    
    return int(re_string,3)