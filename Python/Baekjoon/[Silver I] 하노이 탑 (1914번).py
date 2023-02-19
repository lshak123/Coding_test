#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def hanoi(n,s='1',m='2',e='3'):
    if n == 1:
        print(f'{s} {e}')
    else:
        
        hanoi(n-1,s,e,m)
        print(f'{s} {e}')
        hanoi(n-1,m,s,e)

n = int(input())
print(2**n-1)
if n<=20:
    hanoi(n)

