#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n, m = map(int,input().split())

lst = []
for i in range(n,m+1):
    if i == 1:
        continue
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        lst.append(i)
        
if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))

