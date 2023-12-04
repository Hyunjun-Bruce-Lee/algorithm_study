### https://school.programmers.co.kr/learn/courses/30/lessons/159994

card1 = ["i", "water", "drink"]
card2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]


def solution(card1, card2, goal):
    if len(card2) > len(card1):
        card1, card2 = card2, card1
    card2.extend(['*']*(len(card1)-len(card2)))
    card1, card2 = list(reversed(card1)), list(reversed(card2))
    for target in goal:
        if card1[-1] == target:
            card1.pop()
        elif card2[-1] == target:
            card2.pop()
        else:
            return 'No'
    return 'Yes'

solution(card1, card2, goal)

