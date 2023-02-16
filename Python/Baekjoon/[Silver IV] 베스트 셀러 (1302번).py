#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num = int(input())

dic = {}
for i in range(num):
    book = input()
    if book in dic:
        dic[book] += 1
    else:
        dic[book] = 1

max_list = []        
for i in dic:
    if dic[i] == max(dic.values()):
        max_list.append(i)
        
max_list.sort()
print(max_list[0])

