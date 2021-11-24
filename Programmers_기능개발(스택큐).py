# https://programmers.co.kr/learn/courses/30/lessons/42586

import math
from collections import deque

def solution(progresses, speeds):
    left_job = list(map(lambda x: 100 - x, progresses))
    
    days = deque(list())
    for i,j in zip(left_job, speeds):
        days.append(math.ceil(i/j))
    
    counter_list = list()
    day_stack = list()
    while days:
        day_stack.append(days.popleft())
        if len(days) == 0:
            counter_list.append(len(day_stack))
            day_stack = list()
        elif day_stack[0] >= days[0]:
            continue
        else:
            counter_list.append(len(day_stack))
            day_stack = list()
    return counter_list
