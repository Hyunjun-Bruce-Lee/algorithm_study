### https://programmers.co.kr/learn/courses/30/lessons/72411

## 1차 풀이
from itertools import combinations
from collections import Counter

def solution(orders, course):
    ans = list()
    for i in course:
        temp_list = list()
        for j in orders:
            temp = combinations(sorted(j), i)
            temp_list += temp
        counter = Counter(temp_list)
        if len(counter) != 0 and max(counter.values()) != 1:
            ans += [''.join(f) for f in counter if counter[f] == max(counter.values())]
    return ans
  
## 마지막 답 sort 해야됨

from itertools import combinations
from collections import Counter

def solution(orders, course):
    ans = list()
    for i in course:
        temp_list = list()
        for j in orders:
            temp = combinations(sorted(j), i)
            temp_list += temp
        counter = Counter(temp_list)
        if len(counter) != 0 and max(counter.values()) != 1:
            ans += [''.join(f) for f in counter if counter[f] == max(counter.values())]
    return sorted(ans)
