# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    uniforms = [1 for i in range(n)]
    for i in range(1,n+1):
        if i in lost:
            uniforms[i-1] -= 1
        if i in reserve:
            uniforms[i-1] += 1
    
    for i in range(n-1):
        if (uniforms[i]== 0) & (i != 0):
            if uniforms[i-1] == 2:
                uniforms[i-1] -= 1
                uniforms[i] += 1
            elif uniforms[i+1] == 2:
                uniforms[i+1] -= 1
                uniforms[i] += 1
        elif (uniforms[i]== 0) & (i == 0):
            if uniforms[i+1] == 2:
                uniforms[i+1] -= 1
                uniforms[i] += 1 
    
    if uniforms[-1] == 0:
        if uniforms[-2] == 2:
            uniforms[-2] -= 1
            uniforms[-1] += 1
    
    count = 0
    for i in uniforms:
        if i != 0:
            count += 1
    
    return count
