### https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    temp = str()
    for i in s:
        temp += i
        if temp[-2:] == '()':
            temp = temp[:-2]
    return True if temp == '' else False
