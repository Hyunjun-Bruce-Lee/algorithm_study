### https://school.programmers.co.kr/learn/courses/30/lessons/132267

def solution(a,b,n):
    total_cnt, temp_n = 0, 1
    while temp_n != 0:
        temp_n, temp_r = divmod(n,a)
        temp_n = temp_n*b
        total_cnt += temp_n
        n = temp_n + temp_r
    return total_cnt