### https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3
### 시간 초과
from itertools import combinations
solution = lambda num, k : str(max(map(lambda x : int(''.join(x)),list(combinations(num, len(num) - k)))))

### stack이용한 풀이 통과
def solution(number, k):
    answer = list()
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
    return ''.join(answer[:len(answer) - k])
