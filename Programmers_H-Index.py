### https://programmers.co.kr/learn/courses/30/lessons/42747
## 한국어능력 평가 문제

def solution(citations):
    citations = sorted(citations)
    for i in range(len(citations)):
        if citations[i] >= len(citations)-i:
            return len(citations)-i
    return 0
