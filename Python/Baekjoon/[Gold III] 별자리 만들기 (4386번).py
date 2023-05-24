#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b): 
    a = find(a) 
    b = find(b) 

    if a == b: 
        return
    parent[a] = b
    return

n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(float, input().split())))

parent = [i for i in range(n+1)]

w = []
for i in range(n):
    for j in range(i+1,n):
        w.append([i,j,round(((lst[i][0]-lst[j][0])**2+(lst[i][1]-lst[j][1])**2)**(1/2),2)])
w.sort(key = lambda x:x[2])

cost = 0
for i in w:
    if find(i[0]) != find(i[1]):
        union(i[0],i[1])
        cost += i[2]

print(cost)

