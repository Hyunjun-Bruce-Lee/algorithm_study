### https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def solution(numbers):
    ans = list()
    nums = [i for i in numbers]
    temp = list()
    for j in range(1, len(numbers)+1):
        temp += list(permutations(nums, j))
    new_nums = [int(("").join(t)) for t in temp]

    for n in new_nums:
        if n < 2:
            continue
        check = True            
        for i in range(2,int(n**0.5) + 1):
            if n % i == 0:
                check = False
                break
        if check:
            ans.append(n)

    return len(set(ans))   
