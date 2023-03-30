#!/usr/bin/env python
# coding: utf-8

# In[6]:


word = input()
check_word = {}
for i in word:
    if i in check_word:
        check_word[i] += 1
    else:
        check_word[i] = 1
cnt = 0
result = ''
mid = ''
for k, v in list(check_word.items()):
    if v % 2 == 1:
        cnt += 1
        mid = k
        if cnt >= 2:
            print("I'm Sorry Hansoo")
            break
if cnt<=1:
    for k, v in sorted(check_word.items()):
        result += (k * (v // 2))
    print(result + mid + result[::-1])


# In[ ]:


AA

