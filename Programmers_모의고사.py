### https://school.programmers.co.kr/learn/courses/30/lessons/42840

def counter(answers, ansli):
    cnt = 0
    for idx, ans in enumerate(answers):
        if ans == ansli[idx%len(ansli)]:
            cnt += 1
    return cnt

def solution(answers):
    temp_li = list()
    ans1, ans2, ans3 = [1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]
    for ansli in [ans1,ans2,ans3]:
        temp_li.append(counter(answers, ansli))
    return sorted([id+1 for id, i in enumerate(temp_li) if i == max(temp_li)])
