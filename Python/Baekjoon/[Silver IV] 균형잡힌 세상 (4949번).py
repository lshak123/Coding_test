#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    line = input()
    stack = []
    if line == '.':
        break
    for i in line:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')

