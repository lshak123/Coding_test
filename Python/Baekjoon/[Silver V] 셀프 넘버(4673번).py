#!/usr/bin/env python
# coding: utf-8

# In[ ]:


set_=set(range(1,10001))
set_empty = set()
for i in set_:
    num = i
    sum_num = 0
    for j in range(len(str(i))):
        sum_num += int(str(i)[j])
    set_empty.add(num + sum_num)
a = list(set_-set_empty)
a.sort()
for i in a:
    print(i)

