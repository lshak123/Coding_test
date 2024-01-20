import sys
input= sys.stdin.readline

N = int(input())
m = []
p = []
one = []

for _ in range(N):
    temp = int(input())
    if temp<=0:
        m.append(temp)
    elif temp>1:
        p.append(temp)
    else:
        one.append(temp)

answer = 0
m.sort()
p.sort(reverse=True)

for i in range(len(m)//2):
    answer += m[i*2]*m[i*2+1]
for i in range(len(p)//2):
    answer += p[i*2]*p[i*2+1]
if len(m)%2 == 1:
    answer += m[-1]
if len(p)%2 == 1:
    answer += p[-1]
for i in one:
    answer += i

print(answer)