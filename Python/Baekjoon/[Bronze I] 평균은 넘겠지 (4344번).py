#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num_test = int(input())
for i in range(num_test):
    test = list(map(int, input().split()))
    mean = sum(test[1:])/test[0]
    pct = len([i for i in test[1:] if i > mean])/test[0]
    print('{:.3f}%'.format(pct*100))

