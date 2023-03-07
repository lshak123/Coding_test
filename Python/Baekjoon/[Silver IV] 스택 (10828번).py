#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

N = int(sys.stdin.readline())
Stack = []
for i in range(N) :
    A = sys.stdin.readline().split()

    if A[0] == 'push' : Stack.append(A[1])

    elif A[0] == 'pop' : 
        if Stack : print(Stack.pop())
        else : print(-1)

    elif A[0] == 'size' : print(len(Stack))

    elif A[0] == 'empty' :
        if len(Stack) == 0 : print(1)
        else : print(0)
            
    elif A[0] == 'top' :
        if len(Stack) == 0 : print(-1)
        else : print(Stack[-1])

