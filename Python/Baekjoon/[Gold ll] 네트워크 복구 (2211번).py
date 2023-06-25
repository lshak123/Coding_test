import sys
input = sys.stdin.readline
import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        for i in graph[node]:
            cost = dist + i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                path[i[0]] = node
                heapq.heappush(q, (cost, i[0]))

n, m = map(int, input().split())
path = [0 for _ in range(n+1)]
INF = 999999999
distance = [INF for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


dijkstra(1)

print(n-1)
for i in range(2,n+1):
    print(i,path[i])