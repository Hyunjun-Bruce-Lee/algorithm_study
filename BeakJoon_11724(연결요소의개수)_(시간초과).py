## https://www.acmicpc.net/problem/11724
## 아래코드 시간초과

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

n,m = map(int,input().split())
parent = [i for i in range(0,n+1)]

d_froms = list()
d_tos = list()
for i in range(m):
    dot_from, dot_to = map(int,input().split())
    d_froms.append(dot_from)
    d_tos.append(dot_to)

for i,j in zip(d_froms, d_tos):
    union_parent(parent, i, j)

for i in range(1,n+1):
    find_parent(parent, i)

print(len(set(parent[1:])))
