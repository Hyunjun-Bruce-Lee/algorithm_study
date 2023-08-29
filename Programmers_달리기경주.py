### https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    for name in callings:
        temp = players.index(name)
        players[temp-1], players[temp] = players[temp], players[temp-1]
    return players

# 시간초과


def solution(players, callings):
    temp_dict = {player: idx for idx, player in enumerate(players)}
    for name in callings:
        temp = temp_dict[name]
        players[temp-1], players[temp] = players[temp], players[temp-1]
        temp_dict[players[temp]], temp_dict[players[temp-1]] = temp, temp-1
    return players

# dict를 활용하여 익덱스를 int로 저장하면서 반복문 진행
# index를 찾는 시간 감소 (.index() 대체)
