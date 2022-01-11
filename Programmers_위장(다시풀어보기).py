### https://programmers.co.kr/learn/courses/30/lessons/42578
## 최초풀이, 절반 실패
from itertools import combinations
def solution(clothes):
    
    cloths_dict = dict()
    for i,j in clothes:
        if j not in cloths_dict.keys():
            cloths_dict[j] = 1
        else:
            cloths_dict[j] += 1
    
    
    ans = 0
    for i in range(len(cloths_dict)):
        if len(cloths_dict)-i == 1:
            continue
        temp = list(combinations(cloths_dict.keys(),(len(cloths_dict)-i)))
        for j in temp:
            temp_ans = 1
            for k in j:
                temp_ans *= cloths_dict[k]
        ans += temp_ans
    ans += sum(cloths_dict.values())
    return ans
  
  
## 타인풀이 참고. 다시 풀어보기 권장
def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer: 
          answer[i[1]] += 1
        else: 
          answer[i[1]] = 1

    cnt = 1
    for i in answer.values():
        cnt *= (i+1)
    return cnt - 1
  

## 개쩌는 타인 풀이
from collections import Counter
from functools import reduce
def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
