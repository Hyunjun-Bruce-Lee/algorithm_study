### https://school.programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations

def prime_num(num):
    for i in range(2,int(num/2)):
        if num % i == 0:
            return False
    return True


def solution(nums):
    temp_li = [sum(i) for i in combinations(nums,3)]
    ans_li = list()
    for i in temp_li:
        ans_li.append(prime_num(i))
    return sum(ans_li)