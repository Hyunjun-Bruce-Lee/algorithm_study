# https://programmers.co.kr/learn/courses/30/lessons/43164
# 테스트 케이스 1번 틀림 dont know why
# 아래는 이해는 했지만, 다시풀어보길 권장 (타겟넘버)
# https://programmers.co.kr/learn/courses/30/lessons/43165
def converter(tiket_list):
    re_dict = dict()
    for i in range(len(tiket_list)):
        if tiket_list[i][0] not in re_dict.keys():
            re_dict[tiket_list[i][0]] = [tiket_list[i][1]]
        else:
            re_dict[tiket_list[i][0]].append(tiket_list[i][1])
            re_dict[tiket_list[i][0]].sort()
    for i in set(sum(tiket_list,[])):
        if i not in re_dict.keys():
            re_dict[i] = []
    return re_dict

def solution(tickets):
    tickets_info = converter(tickets)
    stack = [['HOME','ICN']]
    visit_info = list()
    answer = list()
    while stack:
        st_from, st_to = stack.pop()
        if [st_from,st_to] in visit_info:
            continue
        if (tickets_info[st_to] == list()) and (len(answer) != len(tickets)):
            while cross_point != st_from:
                cross_way = tickets_info[cross_point]
                i = 'A'
                for i in cross_way:
                    if [cross_point, i] in visit_info:
                        visit_info.remove([cross_point, i])
                        answer.reverse()
                        answer.remove(i)
                        answer.reverse()
                        cross_point = i
            continue
        visit_info.append([st_from,st_to])
        stack.extend([[st_to, f] for f in reversed(tickets_info[st_to])])
        if len(tickets_info[st_to]) > 1:
            cross_point = st_to
        answer.append(st_to)
    return answer

  
  
tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
test = solution(tickets)
test


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
test = solution(tickets)
test


tickets = [['ICN','A'],['ICN','B'],['B','C'],['C','ICN'],['A','D'],['D','E']]
test = solution(tickets)
test 
