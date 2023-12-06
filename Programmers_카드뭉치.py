### https://school.programmers.co.kr/learn/courses/30/lessons/159994

def solution(card1, card2, goal):
    card1, card2 = list(reversed(card1)), list(reversed(card2))
    for target in goal:
        if card1 and card1[-1] == target:
            card1.pop()
        elif card2 and card2[-1] == target:
            card2.pop()
        else:
            return 'No'
    return 'Yes'