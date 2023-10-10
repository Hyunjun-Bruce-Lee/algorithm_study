### https://school.programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    y = list(str(x))
    z = sum([int(i) for i in y])
    if x%z == 0:
        return True
    else:
        return False



# 아래처럼 한방에도 가능함
def Harshad(n):
    return n%sum(int(x) for x in str(n)) == 0