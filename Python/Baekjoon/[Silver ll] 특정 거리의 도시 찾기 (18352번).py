import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    while q:
        dist, node = heapq.heappop(q)
        
        for i in graph[node]:
            cost =dist+ i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))        

        
n, m, k, x = map(int,input().split())

distance = [9999999]*(n+1)

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b,1))
    
dijkstra(x)
c = 0
for i in range(n+1):
    if distance[i] == k:
        print(i)
        c += 1
if c == 0:
    print(-1)
        