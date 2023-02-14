#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(k, tangerine):
    answer = 0
    lst = [0 for _ in range(max(tangerine))]
    for i in tangerine:
        lst[i-1] += 1
    lst.sort(reverse = True)
    
    sum_ = 0
    while sum_<k:
        sum_+=lst[answer]
        answer += 1
        
    return answer

