
from collections import deque

def bfs(x, dot_n, line_info):
    output_val = list()
    que = deque([x])
    visit_info = [False]*dot_n
    while que:
        x = que.popleft()
        visit_info[x] = True
        if str(x+1) not in output_val:
            output_val.append(str(x+1))
        if x not in line_info.keys():
            continue
        con_dots = line_info[x]
        for i in con_dots:
            if visit_info[i] == False:
                que.append(i)
    return output_val

def dfs(x, dot_n, line_info):
    output_val = list()
    que = [x]
    visit_info = [False]*dot_n
    while que:
        x = que.pop()
        visit_info[x] = True
        if str(x+1) not in output_val:
            output_val.append(str(x+1))
        if x not in line_info.keys():
             continue
        con_dots = line_info[x]
        for i in reversed(con_dots):
            if visit_info[i] == False:
                que.append(i)
    return output_val



dots, lines, start = list(map(int, input().split()))

line_info = dict()
for i in range(lines):
    dot_from, dot_to = list(map(int, input().split()))
    if dot_from-1 in line_info.keys():
        line_info[dot_from-1].append(dot_to-1)
    else:
        line_info[dot_from-1] = [dot_to-1]
    
    if dot_to-1 in line_info.keys():
        line_info[dot_to-1].append(dot_from-1)
    else:
        line_info[dot_to-1] = [dot_from-1]

for i in line_info.keys():
    line_info[i].sort()

B_fs = bfs(start-1,dots,line_info)
D_fs = dfs(start-1,dots,line_info)
print(f"{' '.join(D_fs)}\n{' '.join(B_fs)}")
