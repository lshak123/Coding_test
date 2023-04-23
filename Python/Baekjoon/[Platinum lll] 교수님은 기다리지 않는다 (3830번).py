#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x] == x:
        return x
    else:
        cp = find(parent[x])
        weight[x] += weight[parent[x]]
        parent[x] = cp
        return parent[x]

def union(a, b, w):
    fa = find(a)
    fb = find(b)
    if a != b:
        parent[fb] = fa
        weight[fb] = weight[a] - weight[b] + w;

while True:
    n, m = map(int,input().split())
    if [n, m] == [0,0]:
        break
    parent = [i for i in range(n+1)]
    weight = [0]*(n+1)
    for _ in range(m):
        w = input().split()
        if w[0] == "!":
            union(int(w[1]),int(w[2]),int(w[3]))
        else:
            if find(int(w[1]))!=find(int(w[2])):
                print("UNKNOWN")
            else:
                print(weight[int(w[2])]-weight[int(w[1])])

