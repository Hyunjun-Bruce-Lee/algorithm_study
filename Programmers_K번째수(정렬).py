# https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3

def solution(array, commands):
    answer = []
    for st, en, loc in commands:
        temp = array[st-1:en]
        temp.sort()
        answer.append(temp[loc-1])
    return answer
