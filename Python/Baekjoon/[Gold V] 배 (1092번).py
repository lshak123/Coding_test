#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
cranes = list(map(int,input().split()))
m = int(input())
boxs = list(map(int,input().split()))

cranes.sort(reverse = True)
boxs.sort(reverse = True)

time = 0
while boxs:
    if cranes[0]<boxs[0]:
        break
    for i in cranes:
        for j in boxs:
            if i>=j:
                boxs.remove(j)
                break
    time += 1

print(time) if len(boxs)==0 else print(-1)

