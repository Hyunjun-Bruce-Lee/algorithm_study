### https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    ans,x = str(),n
    if n <= 3:
        ans += '124'[n-1]
    else :
        while x > 3:
            n = x
            x, y = divmod(n-1,3)
            ans += '124'[y]
        ans += '124'[x-1]
    return ''.join(list(reversed(ans)))
