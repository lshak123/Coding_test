#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

