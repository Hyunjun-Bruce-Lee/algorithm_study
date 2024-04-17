### https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(li):
    re = set()
    li = li*2
    for partial_len in range(1,(len(li)//2)+1):
        st_idx = 0
        en_idx = 0+partial_len
        while en_idx != len(li):
            re.add(sum(li[st_idx:en_idx]))
            st_idx += 1
            en_idx += 1
    return len(re)
