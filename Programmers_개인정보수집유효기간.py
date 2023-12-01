### https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    ty,tm,td = map(int,today.split('.'))
    today = ty*12*28 + tm*28 + td
    terms_dict = {k.split()[0]:int(k.split()[1])*28 for k in terms}
    result = list()
    for k,i in enumerate(privacies):
        d,t = i.split()
        yy, mm, dd = list(map(int,d.split('.')))
        ymd = yy*12*28 + mm*28 + dd + terms_dict[t]
        if ymd <= today:
            result.append(k+1)
    return result
