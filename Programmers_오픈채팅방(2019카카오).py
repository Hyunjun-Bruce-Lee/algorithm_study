# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    entry, user_id = list(), list()
    id_name = dict()
    for i in record:
        temp = i.split()
        if temp[0] != 'Change':
            entry.append(temp[0])
            user_id.append(temp[1])
        if len(temp) == 3:
            id_name[temp[1]] = temp[2]
    
    result = list()
    for i,j in zip(entry, user_id):
        if i == 'Enter':
            result.append(f'{id_name[j]}님이 들어왔습니다.')
        elif i == 'Leave':
            result.append(f'{id_name[j]}님이 나갔습니다.')
    return result
