#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N = int(input())
N_lst = input().split()
N_dic = {}
for i in N_lst:
    if i in N_dic:
        N_dic[i] += 1
    else:
        N_dic[i] = 1
M = int(input())
M_lst = input().split()
for i in M_lst:
    if i in N_dic:
        print(N_dic[i], end=" ")
    else:
        print(0 ,end = " ")

