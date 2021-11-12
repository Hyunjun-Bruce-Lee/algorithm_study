def solution(brown, yellow):
    y_candidate = list()
    for i in range(1,yellow+1):
        if yellow%i == 0:
            temp = [i, yellow//i]
            temp.sort()
            temp.reverse()
            y_candidate.append(str(temp[0])+','+str(temp[1]))
    final_y = list()
    for i in set(y_candidate):
        final_y.append(list(map(int, i.split(','))))
    answer = []
    i = [2,1]
    for i in final_y:
        b_val = i[0]*2 + i[1]*2 + 4
        if b_val == brown:
            answer.extend(i)
            break
    answer[0]+=2
    answer[1]+=2
    return answer
