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


planet = []
for i in range(n):
    x,y,z = map(int,input().split())
    planet.append([x,y,z,i])

parent = [i for i in range(n)]

c_lst = []
for i in range(3):
    planet.sort(key = lambda x:x[i])
    for j in range(1,n):
        a = planet[j-1][3]
        b = planet[j][3]
        c_lst.append([abs(planet[j-1][i]-planet[j][i]),a,b])

c_lst.sort(key = lambda x:x[0])

cost = 0
for i in c_lst:
    if find(i[1]) != find(i[2]):
        union(i[1],i[2])
        cost += i[0]
print(cost)

