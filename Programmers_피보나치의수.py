### https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    prev_val_1, prev_val_2 = 0, 1
    flag = 2
    while flag <= n:
        prev_val_3 = prev_val_1 + prev_val_2
        prev_val_1,prev_val_2 = prev_val_2, prev_val_3
        flag += 1
    return prev_val_2%1234567