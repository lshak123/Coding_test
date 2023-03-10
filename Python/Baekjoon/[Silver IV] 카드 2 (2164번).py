#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import deque
n = int(input())
cards = deque([i for i in range(1,n+1)])

while len(cards)>1:
    cards.popleft()
    cards.rotate(-1)
print(cards[0])

