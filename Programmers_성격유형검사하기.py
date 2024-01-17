### https://school.programmers.co.kr/learn/courses/30/lessons/118666

def get_score(ans):
    return ans -4 if ans >= 4 else 4 - ans

def solution(survey,choices):
    char_dict = {'RT' : [0,0], 'CF' : [0,0], 'JM' : [0,0], 'AN' : [0,0]}
    for i,j in zip(survey, choices):
        if j <= 4:
            i = i[0]
        else:
            i = i[-1]
        j = get_score(j)
        for k in char_dict.keys():
            if i in k:
                char_dict[k][k.index(i)] += j
    result = str()
    for k, v in char_dict.items():
        result += k[v.index(max(v))]
    return result