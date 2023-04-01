#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
num = []
for _ in range(n):
    num.append(input())

dic = {}
for i in num:
    for j in range(len(i)):
        if i[j] in dic:
            dic[i[j]] += 10**(len(i)-j-1)
        else:
            dic[i[j]] = 10**(len(i)-j-1)

s_dic = sorted(dic.items(),key=lambda x:x[1],reverse = True)

answer = 0

cnt = 9
for i in s_dic:
    answer += i[1]*cnt
    cnt -=1

print(answer)

