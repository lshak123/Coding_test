#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import heapq
input = sys.stdin.readline

INF = 99999999999
def dijkstra(start):
    q= []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        
        for i in graph[node]:
            cost =dist+ i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

v, e = map(int,input().split())

start = int(input())

graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))


dijkstra(start)

for i in range(1,v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

