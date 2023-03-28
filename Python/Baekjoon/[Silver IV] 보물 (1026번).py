#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
answer = 0

for i in A:
    answer += i*max(B)
    B.remove(max(B))

print(answer)

