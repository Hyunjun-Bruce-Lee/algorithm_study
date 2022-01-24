### https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = len(people)
    people = sorted(people,reverse = True)
    front,back = 0, len(people)-1
    while front < back : 
        if people[front]+people[back] <= limit:
            back -= 1
            answer -= 1
        front += 1
    return answer
