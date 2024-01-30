n = int(input())
line = list(map(int,input().split()))

idx = [0]*(n+1)
for num,i in enumerate(line):
    idx[i] = num

sort_num = 0
cnt = 1
for i in range(1,n):
    if idx[i]<idx[i+1]:
        cnt+=1
    else:
        sort_num = max(sort_num,cnt)
        cnt = 1
print(n-sort_num if n != 1 else 0)