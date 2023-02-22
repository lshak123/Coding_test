#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(cards):
    answer = []
    for i in range(len(cards)):
        lst = []
        while cards[i] not in lst:
            lst.append(cards[i])
            i = cards[i] - 1
        answer.append([] if sorted(lst) in answer else sorted(lst))
    answer.sort(key=len)
    return len(answer[-1]) * len(answer[-2])

