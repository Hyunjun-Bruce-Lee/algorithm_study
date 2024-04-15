### https://school.programmers.co.kr/learn/courses/30/lessons/82612?language=python3

def solution(p,m,c):
    total_p = sum([p*i for i in range(1,c+1)])
    rm = total_p - m
    return rm if rm >=0 else 0


# 아래 처럼 등차수열의 합을 이용하여 푸는게 더 깔끔
def solution(price, money, count):
    temp = money - price*(count*(count+1))/2
    return max(0,-temp)