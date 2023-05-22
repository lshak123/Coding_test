#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    while q:
        dist, node = heapq.heappop(q)
        
        if dist>distance[node]:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))


N = int(input())
M = int(input())
INF = 999999999

distance = [INF]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M): 
    u, v, w = map(int, input().split())
    graph[u].append((v,w))
    
s, e = map(int, input().split())

dijkstra(s)

print(distance[e]-distance[s])

