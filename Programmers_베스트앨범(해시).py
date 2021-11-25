# https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    temp_dict = dict()
    for i,j in zip(genres, plays):
        if i in temp_dict.keys():
            temp_dict[i].append(j)
        else:
            temp_dict[i] = [j]
    
    genres_order = sorted(temp_dict.items(), key = lambda x: sum(x[1]), reverse =True)
    
    temp_list = list()
    for i,_ in genres_order:
        temp_dict[i].sort(reverse = True)
        temp_list.extend(temp_dict[i][:2])
    
    play_list = list()
    for i in temp_list:
        play_list.append(plays.index(i))
        plays[plays.index(i)] = True
    return play_list
