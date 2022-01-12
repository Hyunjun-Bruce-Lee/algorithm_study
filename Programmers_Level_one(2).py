### 두개 뽑아서 더하기
### https://programmers.co.kr/learn/courses/30/lessons/68644
from itertools import combinations
solution = lambda x : sorted(list(set(map(sum,combinations(x,2)))))


### 가운데 글자 가져오기
### https://programmers.co.kr/learn/courses/30/lessons/12903
from math import floor
solution = lambda x : x[floor(len(x)/2):floor(len(x)/2)+1] if len(x)%2 == 1 else x[floor(len(x)/2)-1:floor(len(x)/2)+1]


### 같은 숫자는 싫어
### https://programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    ans = list()
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            continue
        ans.append(arr[i])
    ans.append(arr[-1])    
    return ans
  
  
### 나머지가 1이되는 수 찾기
### https://programmers.co.kr/learn/courses/30/lessons/87389
def solution(n):
    for i in range(1,n):
        if n%i == 1:
            return i
