### https://programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    left, right = 0, 0 
    for i in sizes:
        if max(i) > left:
            left = max(i)
        if min(i) > right:
            right = min(i)
    return int(left*right)

  
 
### https://programmers.co.kr/learn/courses/30/lessons/87377

from itertools import combinations

def get_cross(x,y):
    temp = (x[0]*y[1] - x[1]*y[0])
    x_cor = (x[1]*y[2] - x[2]*y[1])/(temp)
    y_cor = (x[2]*y[0] - x[0]*y[2])/(temp)
    return [x_cor,y_cor]

def solution(test):
    candidates = list(combinations(test,2))

    xs, ys = list(), list()
    for i in candidates:
        if (i[0][0]*i[1][1] - i[0][1]*i[1][0]) == 0:
            continue
        x,y = get_cross(i[0],i[1])
        if x.is_integer() & y.is_integer():
            xs.append(x)
            ys.append(y)

    x_len = int(max(xs) - min(xs) + 1)
    y_len = int(max(ys) - min(ys) + 1)

    ys = [i-min(ys) for i in ys] 
    xs = [i-min(xs) for i in xs] 

    ys = [i+abs(min(ys)) for i in ys] 
    xs = [i+abs(min(xs)) for i in xs] 

    base = [['.']*x_len for _ in range(y_len)]

    for i,j in zip(xs,ys):
        base[int(j)][int(i)] = '*'

    temp = [''.join(i) for i in base]

    return list(reversed(temp))
