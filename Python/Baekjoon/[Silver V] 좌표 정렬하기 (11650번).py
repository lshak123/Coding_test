#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
coor = []
for _ in range(n):
    coor.append(list(map(int,input().split())))


coor.sort()

for i in coor:
    print(i[0], i[1])

