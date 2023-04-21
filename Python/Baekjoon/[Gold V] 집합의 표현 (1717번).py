#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
sys.setrecursionlimit(100000)
n, m = map(int, input().split())

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    parent[x] = y
    return
    
def find(x):
    if parent[x] == x:
        return x
    parent[x]=find(parent[x])
    return parent[x]

parent = [i for i in range(n+1)]

for _ in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        union(a,b)
    else:
        pa = find(a)
        pb = find(b)
        if pa == pb:
            print('YES')
        else:
            print('NO')

