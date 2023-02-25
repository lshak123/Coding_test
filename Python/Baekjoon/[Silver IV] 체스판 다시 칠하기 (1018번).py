#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n, m = map(int, input().split())
board = []
result = []
p = [('WB'*4+"BW"*4)*4, ('BW'*4+"WB"*4)*4]
pan = []

for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        pan = []
        for k in range(i,i+8):
            pan += board[k][j:j+8]
        for l in range(2):
            result.append(sum(ai != bi for ai, bi in zip(pan,[b for b in p[l]])))
            
print(min(result))

