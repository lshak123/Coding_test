#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a, b = map(int,input().split())

num_lst = [True for i in range(b+1)]

for i in range(2,int(math.sqrt(b))+1):
    if num_lst[i] == True:
        j=2
        while i*j <= b:
            num_lst[i*j] = False
            j+=1

for j in range(a,b+1):
    if num_lst[j]:
        if j != 1:
            print(j)

