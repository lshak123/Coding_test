#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = int(input())
lst = []
for i in range(a):
    num = int(input())
    if num == 0:
        lst.pop()
    else:
        lst.append(num)
print(sum(lst))

