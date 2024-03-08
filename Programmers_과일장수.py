### https://school.programmers.co.kr/learn/courses/30/lessons/135808

def solution(k, m, score):
    ans, score = 0, sorted(score, reverse = True)
    
    for i in range(0, len(score), m):
        temp = score[i:i+m]
        
        if len(temp) == m:
            ans += min(temp) * m
    
    return ans