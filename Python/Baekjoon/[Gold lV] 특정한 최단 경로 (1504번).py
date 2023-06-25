import heapq
import sys
input = sys.stdin.readline

n, e = map(int, input().split())

INF = 99999999
graph = [[] for _ in range(n+1)]

def dijkstra(start):
    distance = [INF]*(n+1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    while q:
        dist, node = heapq.heappop(q)
        for i in graph[node]:
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance
                
for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

u, v = map(int,input().split())

dist_ori = dijkstra(1)
dist_u = dijkstra(u)
dist_v = dijkstra(v)

vu = dist_ori[u]+dist_u[v]+dist_v[n]
uv = dist_ori[v]+dist_v[u]+dist_u[n]

result = min(vu, uv)
print(result if result<INF else -1)