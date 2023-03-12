#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
n = int(sys.stdin.readline())
num = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    num.append([x,y])
    
num.sort(key = lambda x: (x[1],x[0]))

for i in num:
    print(i[0],i[1])

