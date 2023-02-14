#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(x):
    answer = True
    sum_ = 0
    num = str(x)
    for i in range(len(num)):
        sum_ += int(num[i])
    if x%sum_ != 0: answer = False
        
    return answer

