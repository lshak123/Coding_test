import sys
input = sys.stdin.readline
n = int(input())
t = []
for _ in range(n):
    t.append(list(map(int,input().split())))

t.sort(key = lambda x:(x[1],x[0]))

end = t[0][1]
answer = 1
for i in t[1:]:
    if i[0]>=end:
        end = i[1]
        answer+=1
print(answer)