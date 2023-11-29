### https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list,report,k):
    reported_cnt = {i:0 for i in id_list}
    report_dict = {i:list() for i in id_list}
    result = list()

    for i in report:
        rep_from, rep_to = i.split()
        report_dict[rep_from].append(rep_to)

    for i in report_dict.keys():
        report_dict[i] = list(set(report_dict[i]))


    for i in sum(list(report_dict.values()), []):
        reported_cnt[i] += 1

    act_report = [key for key, value in reported_cnt.items() if value >= k]

    for name in report_dict.keys():
        temp_cnt = 0
        for temp in act_report:
            if temp in report_dict[name]:
                temp_cnt += 1
        result.append(temp_cnt)
    
    return result


# 아래 풀이가 훨신 깔끔함

def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer