### https://programmers.co.kr/learn/courses/30/lessons/67256

positions = {
    '1' : [0,0],'2' : [0,1],'3' : [0,2],
    '4' : [1,0],'5' : [1,1],'6' : [1,2],
    '7' : [2,0],'8' : [2,1],'9' : [2,2],
    '*' : [3,0],'0' : [3,1],'#' : [3,2]
}

def solution(numbers, hand):
    r_hand = positions['*']
    l_hand = positions['#']
    if hand == 'right': hand = 'R'
    else : hand = 'L'

    result = str()
    for i in numbers:
        i = str(i)
        if positions[i][1] == 0:
            result += 'L'
            l_hand = positions[i]
        elif positions[i][1] == 2:
            result += 'R'
            r_hand = positions[i]
        else:
            x,y = positions[i]
            l_len = abs(l_hand[0] - x) + abs(l_hand[1] - y)
            r_len = abs(r_hand[0] - x) + abs(r_hand[1] - y)
            if l_len == r_len:
                result += hand
                if hand == 'R': r_hand = positions[i]
                else: l_hand = positions[i]
            elif l_len > r_len:
                result += 'R'
                r_hand = positions[i]
            else:
                result += 'L'
                l_hand = positions[i]

    return result
