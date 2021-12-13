### https://www.acmicpc.net/problem/1753

import heapq
import sys

v,e = map(int, sys.stdin.readline().rstrip().split())
start_point = int(sys.stdin.readline().rstrip())

link_info = dict()
for _ in range(e):
    point_from, point_to, cost = map(int, sys.stdin.readline().rstrip().split())
    if point_from in link_info.keys():
        link_info[point_from].append([point_to, cost])
    else:
        link_info[point_from] = [[point_to, cost]]

def path_finder(link_info, num_points, start_point):
    cost_table = [False]*(num_points+1)
    cost_table[start_point] = 0
    temp = list()
    for i in range(len(link_info[start_point])):
        # (cost, from, to)
        heapq.heappush(temp, (link_info[start_point][i][1], start_point, link_info[start_point][i][0]))
    
    while temp:
        t_cost, t_from, t_to = heapq.heappop(temp)
        if not bool(cost_table[t_to]):
            cost_table[t_to] = cost_table[t_from] + t_cost
        else:
            if cost_table[t_to] > cost_table[t_from] + t_cost:
                cost_table[t_to] = cost_table[t_from] + t_cost
        
        if t_to in link_info.keys():
            for i in range(len(link_info[t_to])):
                heapq.heappush(temp, (link_info[t_to][i][1], t_to, link_info[t_to][i][0]))
    return cost_table[1:]

ans = path_finder(link_info, v, start_point)
for i in ans:
    print('INF' if str(i) == 'False' else str(i))
    
### 위코드 메모리 초과, 반례를 통해서 정상 작동은 확인
### 아래의 다익스트라 알고리즘을 이용한 정석풀이와 비교했을때 정석코드의경우 heapq에 to, cost를 저장하지만 본 코드는 form,to,cost를 저장하는것이 원인으로 사료됨


import sys 
import heapq 
input = sys.stdin.readline 
INF = sys.maxsize 
V, E = map(int, input().split()) 
#시작점 K 
K = int(input()) #가중치 테이블 dp 
dp = [INF]*(V+1) 
heap = [] 
graph = [[] for _ in range(V + 1)] 
def Dijkstra(start): 
    #가중치 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화 
    dp[start] = 0 
    heapq.heappush(heap,(0, start)) 
    #힙에 원소가 없을 때 까지 반복. 
    while heap: 
        wei, now = heapq.heappop(heap) 
        #현재 테이블과 비교하여 불필요한(더 가중치가 큰) 튜플이면 무시.
        if dp[now] < wei: 
            continue 
        for w, next_node in graph[now]: 
            #현재 정점 까지의 가중치 wei + 현재 정점에서 다음 정점(next_node)까지의 가중치 W 
            # = 다음 노드까지의 가중치(next_wei) 
            next_wei = w + wei 
            #다음 노드까지의 가중치(next_wei)가 현재 기록된 값 보다 작으면 조건 성립. 
            if next_wei < dp[next_node]: 
                #계산했던 next_wei를 가중치 테이블에 업데이트. 
                dp[next_node] = next_wei 
                #다음 점 까지의 가증치와 다음 점에 대한 정보를 튜플로 묶어 최소 힙에 삽입. 
                heapq.heappush(heap,(next_wei,next_node)) 

#초기화 
for _ in range(E): 
    u, v, w = map(int, input().split()) 
    #(가중치, 목적지 노드) 형태로 저장 
    graph[u].append((w, v)) 

Dijkstra(K) 
for i in range(1,V+1): 
    print("INF" if dp[i] == INF else dp[i])
