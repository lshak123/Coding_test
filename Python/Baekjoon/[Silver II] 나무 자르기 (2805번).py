#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n, m = map(int, input().split())
num = list(map(int,input().split()))
start, end =1, max(num)

while start <= end:
    mid = (start + end)//2
    cut = 0
    for i in num:
        if i>mid:
            cut += i-mid
    if cut >= m:
        start = mid +1
    else:
        end = mid -1
print(end)
