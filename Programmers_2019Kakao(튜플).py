### https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    temp = s[2:-2].split('},{')
    
    temp2 = [list(map(int,i.split(','))) for i in temp]
    
    temp2.sort(key = len)
    
    result = temp2[0]
    
    for i in temp2[1:]:
        result.append(list(set(i) - set(result))[0])

    return result
