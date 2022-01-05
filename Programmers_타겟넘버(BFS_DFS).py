### https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    stack = list()
    idx, ans = 0, 0
    stack.extend([[numbers[0], idx], [-1*numbers[0],idx]])
    while stack:
        sum_num, idx = stack.pop()
        idx += 1
        if idx < len(numbers):
            stack.extend([[sum_num + numbers[idx], idx], [sum_num - numbers[idx], idx]])
        elif (idx == (len(numbers))) & (sum_num == target):
            ans += 1
    return ans
