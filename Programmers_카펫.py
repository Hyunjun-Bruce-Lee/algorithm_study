### https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    for i in range(1,yellow+1):
        a,b = divmod(yellow,i)
        if (b == 0) & ((i*2 + a*2 + 4) == brown):
            return sorted([i+2,a+2], reverse=True)
        else:
            continue