#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
n = int(input())

lst = []
rank = [1 for i in range(n)]
for _ in range(n):
    lst.append(list(map(int,sys.stdin.readline().split())))

for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i][0]<lst[j][0] and lst[i][1]<lst[j][1]:
            rank[i] += 1
for r in rank:
    print(r,end=" ")

