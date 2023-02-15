#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num = int(input())
num_first = num
n = 0
while True:
    if num < 10:
        num = num+num*10
        n +=1
        if num == num_first:
            print(n)
            break
    else:
        num = num%10*10+(num//10+num%10)%10
        n +=1
        if num == num_first:
            print(n)
            break

