#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
point = 0
for i in coin[::-1]:
    if k//i != 0:
        point += k//i
        k = k-(k//i)*i
    if k == 0:
        print(point)
        break

