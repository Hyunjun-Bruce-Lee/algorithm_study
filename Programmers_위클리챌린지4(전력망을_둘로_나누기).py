### https://programmers.co.kr/learn/courses/30/lessons/86971


def link_converter(wires):
    link_dict = dict()
    for i in wires:
        if i[0] in link_dict.keys():
            link_dict[i[0]].append(i[1])
        else:
            link_dict[i[0]] = [i[1]]

        if i[1] in link_dict.keys():
            link_dict[i[1]].append(i[0])
        else:
            link_dict[i[1]] = [i[0]]
    return link_dict


def linked_or_not(wires, wires_cnt):
    visit = [False]*(wires_cnt+1)
    link_dict = link_converter(wires)
    stack = [1]
    while stack:
        temp = stack.pop()
        if (visit[temp] == True)|(temp not in link_dict.keys()):
            visit[temp] = True
        else:
            visit[temp] = True
            for j in link_dict[temp]:
                stack.append(j)
    return visit[1:]

def solution(n, wires):
    wires_cnt = len(list(set(sum(wires,[]))))
    temp = wires.copy()
    ans = 1e+3
    for i in range(len(temp)):
        wires = temp.copy()
        wires.remove(wires[i])
        visit = linked_or_not(wires, wires_cnt)
        new_ans = abs(sum(visit) - (wires_cnt - sum(visit)))
        if new_ans < ans:
            ans = new_ans

    return ans
