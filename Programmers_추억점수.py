### https://school.programmers.co.kr/learn/courses/30/lessons/176963?language=python3

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

def solution(name, yearning, photo):
    answer = []
    temp_dict = {n : y for n, y in zip(name,yearning)}
    for pho in photo:
        temp = [temp_dict[i] for i in pho if  i in temp_dict.keys()]
        answer.append(sum(temp))
    return answer