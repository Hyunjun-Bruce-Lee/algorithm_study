# https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    temp = deque(priorities)
    temp2 = [False]*len(temp)
    temp2[location] = True
    temp2 = deque(temp2)
    
    order = list()
    while True:
        temp_value = temp.popleft()
        temp2_vlaue = temp2.popleft()
        if len(temp) == 0:
            order.append(temp2_vlaue)
            break
        if temp_value >= max(temp):
            order.append(temp2_vlaue)
        else:
            temp.append(temp_value)
            temp2.append(temp2_vlaue)
    
    return order.index(True)+1
