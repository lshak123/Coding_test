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
    else:
        if cost[a]>cost[b]:
            parent[a] = b
        else:
            parent[b] = a

n, m, k = map(int,input().split())
cost = [0]+list(map(int,input().split()))
parent = [i for i in range(n+1)]
for _ in range(m):
    v, w = map(int,input().split())
    union(v,w)
    
answer = 0
for i in range(n+1):
    find(i)
for i in set(parent):
    answer += cost[i]

if answer>k:
    print('Oh no')
else:
    print(answer)

