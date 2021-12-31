## 없는 숫자 더하기
## https://programmers.co.kr/learn/courses/30/lessons/86051?language=python3
def solution(numbers):
    temp = sum(range(10))
    answer = temp - sum(numbers)
    return answer

  
## 예산
## https://programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    d = sorted(d)
    temp,count = 0, 0
    for i in d:
        temp += i
        if temp <= budget:
            count += 1
        else:
            break
    return count
  
  
## 문자열 내림차순 배치하기
## https://programmers.co.kr/learn/courses/30/lessons/12917
solution = lambda x : ''.join(reversed(sorted(list(x))))


## 문자열 다루기 기본
## https://programmers.co.kr/learn/courses/30/lessons/12918
solution = lambda x: True if (x.isnumeric())&((len(x)== 4)or (len(x)== 6)) else False


## 문자열내의 p와 y의 개수
## https://programmers.co.kr/learn/courses/30/lessons/12916
solution = lambda x: True if list(x.upper()).count('P') == list(x.upper()).count('Y') else False
