#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = int(input())
num = 0
for i in range(1, a+1):
    if i<100:
        num += 1
    else:
        if int(str(i)[1]) - int(str(i)[0]) == int(str(i)[2]) - int(str(i)[1]):
            num+=1
print(num)

