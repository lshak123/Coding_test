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

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x]=find(parent[x])
    return parent[x]

G = int(input())
P = int(input())

parent = [i for i in range(G+1)]
count = 0
for i in range(P):
    plane = int(input())
    if find(plane) == 0:
        break
    parent[find(plane)] = parent[find(plane)-1]
    count+=1
    
print(count)
