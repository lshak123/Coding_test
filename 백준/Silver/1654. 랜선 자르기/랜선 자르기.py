K, N = map(int,input().split())
lst = []
for i in range(K):
    lst.append(int(input()))
s, e = 1, max(lst)
while (s<=e):
    mid = (s+e)//2
    cnt = 0
    for i in lst:
        cnt += i//mid
    if cnt<N:
        e = mid-1
    else:
        s = mid+1
print(e)