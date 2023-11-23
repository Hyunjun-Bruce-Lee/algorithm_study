### https://school.programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    arr.remove(min(arr))
    return arr if len(arr) != 0 else [-1]


### 아래코드 기가멕힘
def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]