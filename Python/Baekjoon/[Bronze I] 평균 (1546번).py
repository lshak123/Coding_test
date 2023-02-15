#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num = int(input())
result = list(map(int,input().split()))
mx = max(result)
sum_ = 0
for i in range(num):
    sum_ += result[i]/mx*100
print(sum_/num)

