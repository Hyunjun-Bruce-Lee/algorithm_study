### https://programmers.co.kr/learn/courses/30/lessons/12981
### 공개된 모든 반례 다 통과, 그러나 test case 2,6,7,9,10,13,17,19,20 실패, 왜 인지 모르겠음

import math

def solution(n, words):
    words = list(reversed(words))
    spoken_words = [words.pop()]
    count = 1
    while words:
        next_word = words.pop()
        count += 1
        if (next_word[0] != spoken_words[-1][-1]) | (next_word in spoken_words):
            return [n - (count % n), math.ceil(count / n)]
        else:
            spoken_words.append(next_word)
    return [0,0]


### return [n - (count % n), math.ceil(count / n)] 부분에서 n - (count % n) 부분이 문제
### 다음과 같이 수정 후 통과

def solution(n, words):
    words = list(reversed(words))
    spoken_words = [words.pop()]
    count = 1
    while words:
        next_word = words.pop()
        count += 1
        if (next_word[0] != spoken_words[-1][-1]) | (next_word in spoken_words):
            return [n if count % n == 0 else count % n, math.ceil(count / n)]
        else:
            spoken_words.append(next_word)
    return [0,0]
