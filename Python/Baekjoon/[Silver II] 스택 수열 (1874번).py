#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
stack = []
answer = []
num = 1
for i in range(n):
    m = int(input())
    while num<=m:
        stack.append(num)
        num += 1
        answer.append('+')
    if stack[-1] == m:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        break
if i == n-1:
    for j in answer:
        print(j)

