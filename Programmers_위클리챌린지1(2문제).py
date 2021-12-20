### https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    temp = money - price*(count*(count+1))/2
    if temp < 0 :
        return -temp
    else:
        return 0

# max을 이용한 개선
def solution(price, money, count):
    temp = money - price*(count*(count+1))/2
    return max(0,-temp)
 



### https://programmers.co.kr/learn/courses/30/lessons/82612
from itertools import permutations
def solution(k, dungeons):
    temp = list(range(len(dungeons)))
    cases = list(permutations(temp,len(temp)))
    temp_list = list()
    
    for case in cases:
        t = k
        count = 0
        for j in case:
            least, cost = dungeons[j]
            if least > t:
                break
            else:
                t -= cost
                count += 1
        temp_list.append(count)
    return max(temp_list)
