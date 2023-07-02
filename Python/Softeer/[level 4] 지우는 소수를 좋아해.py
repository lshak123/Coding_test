import sys
input = sys.stdin.readline
import math
import heapq

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
INF = 99999999999999
distance = [INF]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        for node, cost in graph[now]:
            if distance[node] > max(distance[now], cost):
                distance[node] = max(distance[now], cost)
                heapq.heappush(q, (distance[node], node))
                
dijkstra(1)

def isPrime(n):
    if n == 1:
        return True
    if n == 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

distance[-1] += 1
while isPrime(distance[-1]) != True:
    distance[-1] += 1
print(distance[-1])