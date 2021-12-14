### https://programmers.co.kr/learn/courses/30/lessons/72410
### re 사용가능
def solution(sample_id):
    sample_id = sample_id.lower()
    for i in sample_id:
        if i in '~!@#$%^&*()=+[{]}:?,<>/':
            sample_id = sample_id.replace(i, '')

    while '..' in sample_id:
        sample_id = sample_id.replace('..','.')

    if sample_id[0] == '.': 
        sample_id = sample_id[1:]
    if sample_id[-1:] == '.': 
        sample_id = sample_id[:-1]
    if sample_id == '': 
        sample_id = 'a'
    if len(sample_id) >= 16:
        sample_id = sample_id[:15]
        if sample_id[-1] == '.':
            sample_id = sample_id[:-1]
    if len(sample_id) <=2: sample_id += sample_id[-1]*(3-len(sample_id))
    return sample_id


### https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board,moves):
    outs = list()
    boom = 0
    for i in moves:
        location = i-1
        for depth in range(len(board[0])):
            if board[depth][location] != 0:
                outs.append(board[depth][location])
                board[depth][location] = 0
                break
        if (len(outs) > 1):
            if (outs[-1] == outs[-2]):
                del outs[-2:]
                boom += 2
    return boom
