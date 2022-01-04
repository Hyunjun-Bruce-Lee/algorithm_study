### https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(num, target):
    ans = 0
    stack = [[num[0], 0], [-1*num[0], 0]]
    while stack:
        single_num, idx = stack.pop()
        idx += 1
        if (idx == len(num)) & (single_num == target):
            ans += 1
        elif idx < len(num):
            stack.extend([[single_num + num[idx], idx],[single_num - num[idx], idx]])
    return ans
            
