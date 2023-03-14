#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
n, m, b = map(int,sys.stdin.readline().split())

floor = []
for _ in range(n):
    floor.append(list(map(int, sys.stdin.readline().split())))

min_time = 256*500*500
f = 0
for i in range(257):
    time = 0
    get, use = 0, 0
    for x in range(m):
        for y in range(n):
            if floor[y][x]>i :
                get += (floor[y][x]-i)
            else:
                use += (i-floor[y][x])
    if get+b>=use:
        if get*2+use<=min_time:
            min_time = get*2+use
            f = i
print(min_time,f)

