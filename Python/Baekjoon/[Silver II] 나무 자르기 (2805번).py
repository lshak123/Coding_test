#!/usr/bin/env python
# coding: utf-8

# In[69]:


n, m = map(int, input().split())

num = list(map(int,input().split()))

start, end =1, max(num)


# In[73]:


n, m = map(int, input().split())
num = list(map(int,input().split()))
start, end =1, max(num)

while start <= end:
    mid = (start + end)//2
    cut = 0
    for i in num:
        if i>mid:
            cut += i-mid
    if cut >= m:
        start = mid +1
    else:
        end = mid -1
print(end)


# In[72]:


end


# In[46]:


m = 0
for i in num:
    if i > cut:
        m += i - cut


# In[56]:


a


# In[48]:


cut -= 1


# In[33]:


cut


# In[ ]:




