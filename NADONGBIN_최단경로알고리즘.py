## https://www.youtube.com/watch?v=acqm9mM1P6o&t=2s



import heapq
def dijkstra(st):
    q = []
    heapq.heappush(q,(0,st))
    distance[st] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

INF = int(1e9)
n,m,st = map(int,input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))

dijkstra(st)

count = 0
max_distance = 0
for d in distance:
    if d != 1e9:
        count += 1
        max_distance = max(max_distance, d)

print(count -1 , max_distance)
