### https://school.programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    pos, neg = list(), list()
    for i in range(left, right+1):
        temp_cnt = 0
        for j in range(1,i+1):
            if i%j ==0:
                temp_cnt += 1
        if temp_cnt%2 == 0:
            pos.append(j)
        else:
            neg.append(j)
    return sum(pos)-sum(neg)
