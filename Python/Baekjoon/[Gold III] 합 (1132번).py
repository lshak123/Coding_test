#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
num = []
start = set()
for _ in range(n):
    num.append(input())

dic = {}
for i in num:
    start.add(i[0])
    for j in range(len(i)):
        if i[j] in dic:
            dic[i[j]] += 10**(len(i)-j-1)
        else:
            dic[i[j]] = 10**(len(i)-j-1)
            
if len(dic) == 10:
    n_start = []
    for i in dic:
        if i not in start:
            n_start.append(i)

    min_val = max(dic.values())
    for i in n_start:
        if dic[i]<min_val:
            min_val = dic[i]
            min_chr = i
    dic.pop(min_chr)

s_dic = sorted(dic.items(),key=lambda x:x[1],reverse = True)
answer = 0

cnt = 9
for i in s_dic:
    answer += i[1]*cnt
    cnt -=1

print(answer)

