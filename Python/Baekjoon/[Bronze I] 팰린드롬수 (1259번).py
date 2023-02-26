#!/usr/bin/env python
# coding: utf-8

# In[7]:


while True:
    num = input()
    if num == "0":
        break
    elif num == num[::-1]:
        print("yes")
    else:
        print("no")

