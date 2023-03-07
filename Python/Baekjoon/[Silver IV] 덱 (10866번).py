#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

N = int(sys.stdin.readline())
Deque = []
for i in range(N) :
    A = sys.stdin.readline().split()

    if A[0] == 'push_front' : Deque.insert(0,A[1])
    
    elif A[0] == 'push_back' : Deque.append(A[1])

    elif A[0] == 'pop_front' : 
        if Deque : print(Deque.pop(0))
        else : print(-1)
            
    elif A[0] == 'pop_back' : 
        if Deque : print(Deque.pop(-1))
        else : print(-1)

    elif A[0] == 'size' : print(len(Deque))

    elif A[0] == 'empty' :
        if len(Deque) == 0 : print(1)
        else : print(0)
            
    elif A[0] == 'front' :
        if len(Deque) == 0 : print(-1)
        else : print(Deque[0])

    elif A[0] == 'back' :
        if len(Deque) == 0 : print(-1)
        else : print(Deque[-1])

