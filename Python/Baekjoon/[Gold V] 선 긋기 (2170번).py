import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort()
from collections import deque
q = deque(arr[0])
for i in arr[1:]:
    if q[-2]<=i[0]<=q[-1] and q[-1]<=i[1]:
        q.pop()
        q.append(i[1])
    elif q[-1]<i[0]:
        q.append(i[0])
        q.append(i[1])
answer = 0
for i in range(len(q)//2):
    answer += q[i*2+1]-q[i*2]
print(answer)