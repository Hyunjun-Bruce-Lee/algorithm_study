### https://school.programmers.co.kr/learn/courses/30/lessons/250121

map_dict = {"code":0, "date":1, "maximum":2, "remain":3}

def solution(data, ext, val_ext, sort_by):
    temp_data = list()
    for single_row in data:
        if single_row[map_dict[ext]] < val_ext:
            temp_data.append(single_row)
    return sorted(temp_data, key = lambda x: x[map_dict[sort_by]], reverse=False)