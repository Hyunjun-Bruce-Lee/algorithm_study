# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    random_one = [1,2,3,4,5]
    random_two = [2,1,2,3,2,4,2,5]
    random_three = [3,3,1,1,2,2,4,4,5,5]
    cor_list = [0,0,0]
    for i in range(len(answers)):
        one_, two_, three_ = (i%5), (i%8), (i%10)
        if random_one[one_] == answers[i]:
            cor_list[0] += 1
        if random_two[two_] == answers[i]:
            cor_list[1] += 1
        if random_three[three_] == answers[i]:
            cor_list[2] += 1
    temp = max(cor_list)
    answer = []
    for i in range(3):
        if cor_list[i] == temp:
            answer.append(i+1)
    
    answer.sort()

    return answer
