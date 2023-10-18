### https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    holder = list()
    flag = 1
    for i in s:
        if i.isalpha():
            if flag%2 == 0:
                holder.append(i.lower())
            else:
                holder.append(i.upper())
            flag += 1

        else:
            flag = 1
            holder.append(i)

    return ''.join(holder)

