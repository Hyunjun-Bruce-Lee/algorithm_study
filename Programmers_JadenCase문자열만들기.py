### https://programmers.co.kr/learn/courses/30/lessons/12951

## 1차풀이
def solution(string):
    ans = list()
    for i in map(lambda x: x.lower(), test.split()):
        if i[0].isalpha():
            ans.append(i[0].upper() + i[1:])
        else:
            ans.append(i)
    return ' '.join(ans)
## 실패, 원본 문자열 공백 개수 유지되어야함


## 2차풀이
def solution(string):
    ans = list()
    for i in string.split(' '):
        if i != '':
            ans.append(i[0].upper() + i[1:].lower())
        else:
            ans.append(i)
    return ' '.join(ans)
## 통과


## 한줄코딩
solution = lambda x: " ".join([(i[0].upper() + i[1:].lower()) if i != '' else "" for i in test.split(' ')])
