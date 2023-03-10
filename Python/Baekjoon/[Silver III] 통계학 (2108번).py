#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

n = int(input())

num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))

num.sort(reverse = True)

print(round(sum(num)/n))

print(num[n//2])

dic = {}
for i in num:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

lst = sorted(dic.items(), key=lambda x: x[1])

if len(num)>1:
    if lst[-1][1] == lst[-2][1]:
        print(lst[-2][0])
    else:
        print(lst[-1][0])
else:
    print(num[0])

print(max(num)-min(num))

