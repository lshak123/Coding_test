#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

n = int(input())

words = []
for _ in range(n):
    words.append(sys.stdin.readline().strip())

words = list(set(words))

words.sort()

words.sort(key = lambda x: len(x))

for i in words:
    print(i)

