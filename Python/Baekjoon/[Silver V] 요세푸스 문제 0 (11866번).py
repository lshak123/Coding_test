#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n, k = map(int,input().split())

lst = [i for i in range(1,n+1)]
answer = []

idx = 0
while lst:
    idx += k-1
    if idx >= len(lst):
        idx %= len(lst)
    answer.append(str(lst.pop(idx)))

print("<", ", ".join(answer), ">", sep="")


# In[ ]:


from collections import deque

n, k = map(int,input().split())
answer = []

deq = deque([i for i in range(1,n+1)])
for _ in range(n):
    deq.rotate(-2)
    answer.append(str(deq.popleft()))

print("<", ", ".join(answer), ">", sep="")

