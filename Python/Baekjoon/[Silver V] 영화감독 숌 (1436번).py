#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
num = 666
while True:
    if '666' in str(num):
        n -=1
        if n == 0:
            print(num)
            break
        num+=1
    else:
        num+=1

