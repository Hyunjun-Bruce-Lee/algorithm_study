### https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    temp_dict = dict()
    ans = list()
    for idx in range(len(s)):
        cur_char = s[idx]
        if cur_char in temp_dict.keys():
            ans.append(idx - temp_dict[cur_char])
            temp_dict[cur_char] = idx
        else:
            temp_dict[cur_char] = idx
            ans.append(-1)
    return ans
