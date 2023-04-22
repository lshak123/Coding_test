#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x]=find(parent[x])
    return parent[x]

def union(a, b): 
    a = find(a) 
    b = find(b) 

    if a == b: 
        return
    parent[a] = b
    return

n, m, k = map(int,input().split())
power = list(map(int,input().split()))
parent = [i for i in range(n+1)]
lst = []

for i in power:
    parent[i] = 0
    
for _ in range(m):
     lst.append(list(map(int, input().split())))

        
lst.sort(key = lambda x:x[2])

cost = 0

for i in lst:
    if find(i[0]) != find(i[1]):
        union(i[0],i[1])
        cost+=i[2]
        
print(cost)

