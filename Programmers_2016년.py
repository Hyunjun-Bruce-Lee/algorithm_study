### https://school.programmers.co.kr/learn/courses/30/lessons/12901
# datetime 모듈 이용하면 간단하지만 사용하지 않고 풀이

days_str = ["THU","FRI","SAT","SUN","MON","TUE","WED"]

def get_days(m):
    if m <= 7:
        if m == 2:
            days = 29
        elif m%2 == 0:
            days = 30
        else:
            days = 31
    else:
        if m%2 == 0:
            days = 31
        else:
            days = 30
    return days

def solution(a,b):
    days = 0
    for i in range(1,a):
        days += get_days(i)
    return days_str[(days+b)%7]

#### 아래가 더깔끔한듯
def getDayName(a,b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return day[(sum(month[:a-1])+b-1)%7]