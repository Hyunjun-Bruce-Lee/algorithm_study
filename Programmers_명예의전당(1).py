### https://school.programmers.co.kr/learn/courses/30/lessons/138477

def solution(k,score):
    ranking, answer = list(), list()
    for s in score:
        ranking.append(s)
        ranking.sort(reverse=True)
        answer.append(ranking[:k][-1])
    return answer
