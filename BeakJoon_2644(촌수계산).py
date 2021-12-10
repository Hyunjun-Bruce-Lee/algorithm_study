## https://www.acmicpc.net/problem/2644

n_pop = int(input())
tar_a, tar_b = list(map(int, input().split()))
n_relation = int(input())
p_list, c_list = list(), list()
for _ in range(n_relation):
    p, c = map(int, input().split())
    p_list.append(p)
    c_list.append(c)


ap, bp = tar_a, tar_b
app, bpp = [ap], [bp]
flag = True
while flag:
    if ap in c_list:
        ap = p_list[c_list.index(ap)]
        app.append(ap)
    
    if bp in c_list:
        bp = p_list[c_list.index(bp)]
        bpp.append(bp)

    if (ap in bpp):
        ans = len(app)-1 + bpp.index(ap)
        flag = False
    elif (bp in app):
        ans = len(bpp)-1 + app.index(bp)
        flag = False
    elif (ap not in c_list)&(bp not in c_list):
        ans = -1
        flag = False
print(ans)
    
