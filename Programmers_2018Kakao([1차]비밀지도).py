### https://programmers.co.kr/learn/courses/30/lessons/17681

class converter:
    def __init__(self, n):
        self.n = n    
    def __call__(self, num):
        num = bin(num)[2:]
        if len (num) < self.n:
            num = '0'*(self.n - len(num)) + num
        return num

def decript(ar1,ar2,n):
    result = list()
    for i,j in zip(ar1,ar2):
        temp = str()
        for idx in range(n):
            if (i[idx] == '1') | (j[idx] == '1'):
                temp += '#'
            else:
                temp += ' '
        result.append(temp)
    return result


def solution(n, arr1, arr2):
    Conve = converter(n)
    arr1 = list(map(Conve, arr1))
    arr2 = list(map(Conve, arr2))
    return decript(arr1,arr2,n)
