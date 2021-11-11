
def match_find(word, words, step):
    candidates = list()
    step += 1
    for i in words:
        count = 0
        for j in range(len(i)):
            if i[j] == word[j]:
                count += 1
        if count == len(word) - 1:
            candidates.append([i,step])
    return candidates

# def match_find(word, words, step):
#     candidates = list()
#     step += 1
#     for i in words:
#         if sum([x != y for x,y in zip(word,i)]) == 1:
#             candidates.append([i,step])
#     return candidates

from collections import deque
def bfs(begin,target,words):
    if target not in words:
        return 0
    que = deque()
    words.append(begin)
    que.append([begin,0])
    visit_info = [False]*(len(words)+1)
    while que:
        x, step = que.popleft()
        if visit_info[words.index(x)] == True:
            continue
        elif x == target:
            return step
        que.extend(match_find(x, words, step))

begin = 'hit'
target = 'cog'
words = ['hot','dot','dog','lot','log','cog']

bfs(begin, target, words)
