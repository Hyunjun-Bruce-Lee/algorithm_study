### https://school.programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1,arr2):
    temp = arr1
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            temp[i][j] = arr1[i][j] + arr2[i][j]
    return temp