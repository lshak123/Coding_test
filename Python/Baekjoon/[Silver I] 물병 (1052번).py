#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n, k = map(int,input().split())

count = 0
while bin(n).count('1')>k:
    n+=1
    count += 1

print(count)

