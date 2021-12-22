### https://programmers.co.kr/learn/courses/30/lessons/84512

from itertools import product
solution = lambda word: sorted(list(set(map(lambda x: ''.join(x).replace('0',''),list(product(['0','A','E','I','O','U'], repeat = 5)))))).index(word)


### https://programmers.co.kr/learn/courses/30/lessons/84021

### 미결 조각을 빼서 비교하는 이이디어(st x, en x, xt y, en y 4가지를 이용하여 조각 추출)
