### https://school.programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    return sum([a[i]*b[i] for i in range(len(a))])


### zip이 더 괜찮은듯
def solution(a,b):
    return sum([x*y for x, y in zip(a,b)])