import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = 999999999

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b,w))

def dijkstra(start):
    distance = [INF]*(n+1)
    q = []
    heapq.heappush(q,(0,start, [start]))
    distance[start] = 0
    while q:
        dist, node, lst = heapq.heappop(q)
        if lst[-1] == end:
            break
        for i in graph[node]:
            cost = dist + i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0],lst+[i[0]]))
    return distance, lst
                
start, end = map(int,input().split())

distance, lst = dijkstra(start)
print(distance[end])
print(len(lst))
for i in lst:
    print(i, end = " ")