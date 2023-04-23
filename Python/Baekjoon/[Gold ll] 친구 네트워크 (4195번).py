#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a!=b:
        parent[b] = a
        number[a] += number[b]

n = int(input())
for i in range(n):
    parent = dict()
    number = dict()
    m = int(input())
    for i in range(m):
        x, y = input().split()

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        union(x,y)
        print(number[find(x)])

