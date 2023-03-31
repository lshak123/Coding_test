#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
lst = list(map(int,input().split()))
s = int(input())

for i in range(n-1):
    max_n = max(lst[i:i+s+1])
    s = s - (lst.index(max_n)-i)
    lst.insert(i,lst.pop(lst.index(max_n)))
    if s == 0:
        break

for i in lst:
    print(i, end = " ")

