### https://programmers.co.kr/learn/courses/30/lessons/62048

from math import gcd
def solution(w,h):
    return (w*h) - (w+h-gcd(w,h))


## OR ##

from math import gcd
solution = lambda x,y: (x*y) - (x+y-gcd(x,y))
