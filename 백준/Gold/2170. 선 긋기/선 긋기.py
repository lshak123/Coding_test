import sys
input = sys.stdin.readline
n = int(input())
lines = []
for _ in range(n):
    lines.append(list(map(int,input().split())))
lines.sort()
l, r = lines[0]
answer = r-l

for s,e in lines[1:]:
    if s<=r:
        if e>=r:
            answer += e-r
            r = e
        else:
            continue
    else:
        answer += e-s
        l, r = s, e
        
print(answer)