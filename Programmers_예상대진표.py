### https://programmers.co.kr/learn/courses/30/lessons/12985
## 1차 풀이
def solution(num_attend, A, B):
    while True:
        attendent = range(1,num_attend+1)
        if (A in attendent) & (B in attendent):
            num_attend = int(num_attend/2)
        elif (A in attendent) | (B in attendent):
            ans = len(bin(num_attend)[2:])
            break
    return ans
## 시간초과

## 2차풀이
def solution(num_attend, A, B):
    while True:
        if (A <= num_attend) & (B <= num_attend):
            num_attend = int(num_attend/2)
        elif (A <= num_attend) | (B <= num_attend):
            ans = len(bin(num_attend)[2:])
            break
    return ans
## range를 이용한 포함여부 확인 대신 단순 수치 비교로 소요시간 줄임
## 그래도 시간초과

## 3차풀이
import math
def solution(num_attend, A, B):
    for i in range(1,int(math.log2(num_attend))+1):
        if (A <= 2**i) & (B <= 2**i):
            break
    return i
## 주어진 num_attend가 2의 20승 이하인것에 착안, while을 돌리기보다 20까지 for를 돌리기로함
## 시간초과 해결, 그러나 A가 항상 초기 대진에 포함되지 않을경우 고려 못함. (2^3 <= A,B <= 2^4)
## 답이 틀림

## 4차풀이
def solution(num_attend,A,B):
    answer = 0
    while A!= B:
        A, B = (A+1)//2, (B+1)//2
        answer+=1
    return answer
## 단순히 나눠가며 몫을 계산하면 됨. 
