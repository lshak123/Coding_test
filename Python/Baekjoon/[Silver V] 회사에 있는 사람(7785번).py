#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num = int(input())

staff = {}
for i in range(int(num)):
    a, b = map(str,input().split())
    if b == 'enter':
        staff[a] = 'enter'
    else:
        del staff[a]
        
staff = sorted(staff, reverse = True)
for i in staff:
    print(i)

