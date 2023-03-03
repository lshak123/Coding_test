#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N = int(input())
A = set(map(int,input().split()))
M = int(input())
num = list(map(int,input().split()))

for i in num:
    print(1) if i in A else print(0)

