#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

parent = [i for i in range(n)]

def find(x):
    if x == parent[x]:
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

for i in range(n):
    link = list(map(int,input().split()))
    for j in range(n):
        if link[j] == 1:
            union(i,j)

plan = list(map(int,input().split()))
result = set()
for i in plan:
    result.add(find(i-1))
if len(result) == 1:
    print("YES")
else:
    print("NO")

