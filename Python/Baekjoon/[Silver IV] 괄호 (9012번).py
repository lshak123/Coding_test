#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = int(input())
for j in range(a):
    lst = []
    k = input()
    for i in k:
        if i == '(':
            lst.append(i)
        elif i == ')':
            if len(lst) == 0:
                print('NO')
                break
            else:
                lst.pop()
    else:
        if len(lst) > 0:
            print('NO')
        else:
            print('YES')

