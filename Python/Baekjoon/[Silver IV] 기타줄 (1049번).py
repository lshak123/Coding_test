#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n, m = map(int,input().split())
answer = 0
one = []
six = []
for _ in range(m):
    a,b = map(int,input().split())
    six.append(a)
    one.append(b)

min1 = min(one)
min6 = min(six)

if min6>=min1*6:
    answer = min1*n
else:
    if min6<=(n%6)*min1:
        answer = (n//6+1)*min6
    else:
        answer = (n//6)*min6+(n%6)*min1
print(answer)

