def link_converter(link_info):
    link_dict = dict()
    for i in range(len(link_info)):
        for j in range(len(link_info[i])):
            if link_info[i][j]:
                if i not in link_dict.keys():
                    link_dict[i] = [j]
                else:
                    link_dict[i].append(j)
    return link_dict

def link_finder(link_dict, start, visit_info):
    stack = [start]
    while stack:
        com = stack.pop()
        if not visit_info[com]:
            visit_info[com] = True
            stack.extend(link_dict[com])

def solution(n, computers):
    count =  0
    link_dict = link_converter(computers)
    visit_info = [False]*n
    for i in range(n):
        if visit_info[i] == False:
            start = i
        else:
            continue
        link_finder(link_dict, start, visit_info)
        count += 1
    return count
