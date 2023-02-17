#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n= int(input())
num = 0
while True:
    if n%5 == 0:
        num += n//5
        print(num)
        break
    else:
        n -= 3
        num += 1
        if n < 0:
            print(-1)
            break

