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

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]

arr = []

for _ in range(m):
    arr.append(list(map(int, input().split())))
    
arr.sort(key = lambda x:x[2])

cost = 0
for i in arr:
    if find(i[0]) != find(i[1]):
        union(i[0],i[1])
        cost += i[2]

print(cost)

