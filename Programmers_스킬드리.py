### https://school.programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    count = 0
    for single_tree in skill_trees:
        s = str()
        for cur in single_tree:       
            if cur in skill:
                s += cur
        if skill[:len(s)] == s:
            count += 1
    return count