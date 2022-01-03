### https://programmers.co.kr/learn/courses/30/lessons/17677

def converter(input_string):
    return_list = list()
    for i in range(len(input_string)-1):
        temp = input_string[i:i+2]
        if temp.isalpha():
            return_list.append(temp)
    return return_list

def inter(in_a,in_b):
    A, B = in_a.copy(), in_b.copy()
    return_list = list()
    if len(A) < len(B):
        A , B = B, A
    for i in B:
        if i in A:
            return_list.append(i)
            A.remove(i)
    return return_list

def outer(in_a,in_b):
    A,B = in_a.copy(), in_b.copy()
    if len(A) < len(B):
        A , B = B, A    
    for i in A:
        if i in B:
            B.remove(i)
    return A+B


def solution(A,B):
    A, B = converter(A.upper()), converter(B.upper())
    return int((len(inter(A,B))/len(outer(A,B)))*65536) if len(outer(A,B)) != 0 else 65536
