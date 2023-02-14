#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(new_id):
    rule2 = ['a','b',"c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",".","1","2","3","4","5","6","7","8","9","0","-","_",]
    answer = ""
    new_id = new_id.lower()
    for i in new_id:
        if i in rule2:
            answer += i
    while ".." in answer:
        answer = answer.replace('..','.')
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1] 
    if answer == "":
        answer = "a"
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    while len(answer) < 3:
        answer += answer[-1]
    return answer

