#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(price, money, count):
    t = 0
    for i in range(1, count+1):
        t += price*i
    answer = money - t
    if answer > 0:
        answer = 0
    else:
        answer = -answer
    return answer

