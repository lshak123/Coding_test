#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
for _ in range(n):
    paper, num = map(int,input().split())
    lst = input().split()

    count = 1
    idx = [0]*paper
    idx[num] = 'target'

    while True:
        if lst[0] == max(lst):
            if idx[0] == 'target':
                print(count)
                break
            else:
                idx.pop(0)
                lst.pop(0)
                count += 1
        else:
            lst.append(lst.pop(0))
            idx.append(idx.pop(0))

