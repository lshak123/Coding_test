#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
lst = list(map(int,input().split()))

count = 0
for i in lst:
    num = True
    for j in range(2,int(i**(1/2))+1):
        if i%j == 0:
            num = False
    if i != 1 and num == True:
        count +=1
print(count)

