#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a, b = map(int, input().split())
num = 1
num_lst = []
for i in range(a):
    num_lst.append(int(input()))
    
start, end = 1, max(num_lst)
while start <= end:
    count = 0
    mid = (start+end)//2
    for i in num_lst:
        count += i // mid
    if count<b:
        end = mid -1
    else:
        start = mid +1
print(end)

