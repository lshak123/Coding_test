#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
in_lst, out_lst = [], []
answer = [0 for i in range(n)]
for i in range(2*n):
    a = input()
    in_lst.append(a) if i<n else out_lst.append(a)

for i in range(n):
    for j in range(i,n):
        if in_lst.index(out_lst[i])>in_lst.index(out_lst[j]):
            answer[i] = 1
print(sum(answer))

