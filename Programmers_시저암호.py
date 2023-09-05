### https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ""
    for i in s:
        if i.isalpha():
            if i.islower():
                temp = ord(i) + n
                if temp > 122:
                    temp -= 26 
            else: 
                temp = ord(i) + n
                if temp > 90:
                    temp -= 26
        else:
            temp = ord(i)
        answer += chr(temp)
    return answer