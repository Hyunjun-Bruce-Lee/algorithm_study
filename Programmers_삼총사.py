### https://school.programmers.co.kr/learn/courses/30/lessons/131705

from itertools import combinations

def solution(number):
    ans = [i for i in combinations(number, 3) if sum(i) == 0]
    return len(ans)