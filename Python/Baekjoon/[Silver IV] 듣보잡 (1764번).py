#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a,b = map(int,input().split())

eme = []
qh = []
for i in range(a):
    eme.append(input())
for i in range(b):
    qh.append(input())
emeqh = sorted(list(set(eme) & set(qh)))
print(len(emeqh))
for i in emeqh:
    print(i)

