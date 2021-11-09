
n_com = int(input())
n_link = int(input())
link_info = dict()
for _ in range(n_link):
    f_rom, t_o = list(map(int, input().split()))
    if f_rom not in link_info.keys():
        link_info[f_rom] = [t_o]
    else:
        link_info[f_rom].append(t_o)
    
    if t_o not in link_info.keys():
        link_info[t_o] = [f_rom]
    else:
        link_info[t_o].append(f_rom)

def dfs(start, link_info, n_dots):
    count = 0
    visit_info = [False]*(n_dots+1)
    stack = [start]
    while stack:
        x = stack.pop()
        
        if visit_info[x] == False:
            visit_info[x] = True
            count += 1
            stack.extend(link_info[x])
    return count

print(dfs(1, link_info, n_com)-1)
