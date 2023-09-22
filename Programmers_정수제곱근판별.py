### https://school.programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    temp = n**(1/2)
    temp, flag = str(temp).split('.')
    if flag == '0':
        return (int(temp)+1)**2
    else:
        return -1


### 소수 를 1로 나누면 소수점 아래가 나머지로 남음
### 이걸 이용해서 하는게 더 좋은듯

def solution(n):
    temp = n**(1/2)

    if temp % 1 == 0:
        return (int(temp)+1)**2
    else:
        return -1
