### https://programmers.co.kr/learn/courses/30/lessons/70129

from collections import Counter

def solution(s):
    zeros, count = 0, 0
    while s != '1':
        zeros += Counter(s)['0']
        s = bin(len(s.replace('0','')))[2:]
        count += 1
    return [count, zeros]
